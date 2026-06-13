"""CLI: crawl the Azure Pricing Calculator and learn selector schemas.

Usage:
  uv run learn.py --list                         # discover products only
  uv run learn.py --all                          # learn every product (long!)
  uv run learn.py --products "Virtual Machines,Azure Backup,Managed Disks"
  uv run learn.py --all --headless --force
"""
import argparse
import json
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from azcalc.driver import get_driver
from azcalc.learner import SchemaLearner


def main():
    ap = argparse.ArgumentParser(description="Self-learning Azure calculator mapper")
    ap.add_argument("--list", action="store_true", help="only discover and list products")
    ap.add_argument("--all", action="store_true", help="learn every discovered product")
    ap.add_argument("--products", help="comma-separated product names (substring match)")
    ap.add_argument("--max", type=int, default=None, help="cap number of products")
    ap.add_argument("--force", action="store_true", help="re-learn existing schemas")
    ap.add_argument("--headless", action="store_true")
    ap.add_argument("--schemas", default="schemas", help="output directory")
    ap.add_argument("--no-interact", action="store_true",
                    help="skip the interactive option sweep (faster, shallower)")
    ap.add_argument("--no-nested", action="store_true",
                    help="skip the nested (combination) sweep — only change one "
                         "field at a time (faster, misses combo-gated fields like "
                         "SQL Server License per OS)")
    ap.add_argument("--max-options", type=int, default=16,
                    help="only sweep selects with at most this many options "
                         "(16 covers e.g. the 14-entry Linux VM Type list; "
                         "region/instance lists stay excluded)")
    args = ap.parse_args()

    driver = get_driver(headless=args.headless)
    try:
        learner = SchemaLearner(driver, schema_dir=args.schemas)
        if args.list:
            learner.open_calculator()
            products = learner.discover_products()
            print(json.dumps(products, indent=2))
            print(f"\n{len(products)} products discovered")
            return
        only = [p.strip() for p in args.products.split(",")] if args.products else None
        if not args.all and not only:
            ap.error("use --list, --all, or --products")
        learner.learn_all(
            only=only, force=args.force, max_products=args.max,
            interact=not args.no_interact, max_options=args.max_options,
            nested=not args.no_nested,
        )
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
