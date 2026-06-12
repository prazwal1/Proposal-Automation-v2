"""Convert v1 assessment JSON (data/assesment*.json) into the generic
component config consumed by engine.py, so existing files keep working.
"""


def _vm_component(vm, reservation=None):
    fields = {
        "Region": vm["region"],
        "Operating system": "Windows" if "Windows" in vm.get("os", "") else "Linux",
    }
    if vm.get("type"):
        fields["Type"] = vm["type"]
    if vm.get("tier"):
        fields["Tier"] = vm["tier"]
    if vm.get("license"):
        fields["License"] = vm["license"]
    if vm.get("instance"):
        instance = vm["instance"].replace("_", " ").replace("Standard ", "")
        fields["size"] = instance
    if vm.get("quantity"):
        fields["Virtual machines"] = vm["quantity"]
    if reservation == 1:
        fields["computeBillingOption"] = "one-year"
    elif reservation == 3:
        fields["computeBillingOption"] = "three-year"

    os_disk = vm.get("os_disk")
    if isinstance(os_disk, dict) and os_disk.get("tier") and os_disk.get("size"):
        fields["managedDiskTier"] = os_disk["tier"]
        fields["managedDiskType"] = os_disk["size"]
        fields["managedDisks"] = os_disk.get("quantity", 1)
        if os_disk.get("redundancy"):
            fields["managedDiskRedundancy"] = os_disk["redundancy"]

    return {"product": "Virtual Machines", "name": vm["name"], "fields": fields}


def _data_disk_component(vm, disk, index):
    fields = {
        "Region": vm["region"],
        "Disk tier": disk["tier"],
        "Disk size": disk["size"],
        "Disks": disk.get("quantity", 1),
    }
    if disk.get("redundancy"):
        fields["Redundancy"] = disk["redundancy"]
    return {
        "product": "Managed Disks",
        "name": f"{vm['name']}_DataDisk{index}",
        "fields": fields,
    }


def assessment_to_config(assessment, disks=True, backup=False, reservation=None):
    components = []
    for vm in assessment.get("vms", []):
        components.append(_vm_component(vm, reservation))
        if disks:
            for i, disk in enumerate(vm.get("data_disks", []), start=1):
                components.append(_data_disk_component(vm, disk, i))
        if backup and vm.get("backup"):
            b = vm["backup"]
            fields = {
                "Region": vm["region"],
                "VMs": b.get("vms", 1),
                "GB": b.get("size_gb"),
            }
            components.append(
                {"product": "Azure Backup", "name": f"{vm['name']}_Backup", "fields": fields}
            )
    return {
        "estimate_name": assessment.get("estimate_name"),
        "components": components,
    }
