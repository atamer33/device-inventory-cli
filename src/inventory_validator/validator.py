from pathlib import Path
import yaml
from inventory_validator.models import Inventory


def load_inventory(path: str | Path) -> Inventory:
    path = Path(path)
    raw = yaml.safe_load(path.read_text())
    return Inventory.model_validate(raw)



def check_duplicates(inventory: Inventory) -> None:
    seen_names: set[str] = set()
    seen_ips: set[str] = set()

    for device in inventory.devices:
        name = device.name
        ip = str(device.mgmt_ip)  # IPvAnyAddress -> string for the set

        if name in seen_names:
            raise ValueError(f"duplicate name: {name}")
        if ip in seen_ips:
            raise ValueError(f"duplicate mgmt_ip: {ip}")

        seen_names.add(name)
        seen_ips.add(ip)


        