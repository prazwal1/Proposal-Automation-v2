"""CLI: build an estimate in the Azure Pricing Calculator from a JSON config
using the learned schemas.

Usage:
  uv run build.py configs/example_estimate.json
  uv run build.py ../data/assesment.json --v1            # old assessment format
  uv run build.py config.json --export --download Azure_Estimates
"""
import argparse
import json
import sys
import time

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from azcalc.adapter import assessment_to_config
from azcalc.driver import get_driver
from azcalc.engine import GenericEngine


def main():
    ap = argparse.ArgumentParser(description="Generic Azure calculator estimate builder")
    ap.add_argument("config", help="path to estimate config JSON")
    ap.add_argument("--v1", action="store_true", help="config is a v1 assessment JSON")
    ap.add_argument("--reservation", type=int, choices=[1, 3], default=None)
    ap.add_argument("--no-disks", action="store_true", help="(v1) skip data disks")
    ap.add_argument("--backup", action="store_true", help="(v1) include backup components")
    ap.add_argument("--schemas", default="schemas")
    ap.add_argument("--headless", action="store_true")
    ap.add_argument("--export", action="store_true", help="export estimate as Excel")
    ap.add_argument("--download", default="Azure_Estimates")
    ap.add_argument("--keep-open", type=int, default=0,
                    help="seconds to keep the browser open after building")
    args = ap.parse_args()

    with open(args.config, encoding="utf-8") as f:
        config = json.load(f)
    if args.v1 or "vms" in config:
        config = assessment_to_config(
            config,
            disks=not args.no_disks,
            backup=args.backup,
            reservation=args.reservation,
        )

    driver = get_driver(download_path=args.download, headless=args.headless)
    try:
        engine = GenericEngine(driver, schema_dir=args.schemas)
        engine.build(config)
        if args.export:
            path = engine.export_excel(
                download_path=args.download,
                rename_to=config.get("estimate_name"),
            )
            print(f"📥 Exported: {path}" if path else "⚠️  Export did not complete")
        if args.keep_open:
            time.sleep(args.keep_open)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
