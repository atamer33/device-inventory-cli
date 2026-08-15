import sys
from inventory_validator.validator import load_inventory, check_duplicates


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python -m inventory_validator.cli <inventory.yaml>")
        sys.exit(2)

    path = sys.argv[1]
    try:
        inv = load_inventory(path)
        check_duplicates(inv)
        print(f"OK: {len(inv.devices)} devices")
#In Python, errors are organized in a family tree. Exception is the parent class of almost all standard errors (like FileNotFoundError, KeyError, ValueError, or TypeError).
#This creates a temporary variable (named e) that holds the actual error object
    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()