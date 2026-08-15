import pytest
import subprocess
import sys
from pydantic import ValidationError
from inventory_validator.validator import load_inventory, check_duplicates




@pytest.mark.parametrize(
    "bad_file, expected_error_snippet",
    [
        ("tests/fixtures/invalid_role.yaml", "role"),
        ("tests/fixtures/duplicate_name.yaml", "duplicate name"),
        ("tests/fixtures/duplicate_ip.yaml", "duplicate mgmt_ip"),
        ("tests/fixtures/missing_ip.yaml", "value is not a valid ipv4 or ipv6 address")

    ],
)

def test_various_invalid_files(bad_file, expected_error_snippet):
    """Feeds multiple bad files into one test to save space and code duplication."""
    with pytest.raises((ValidationError, Exception)) as excinfo:
        load_inventory(bad_file)
        inv = load_inventory(bad_file)
        check_duplicates(inv)
        Inv = load_inventory(bad_file)
        check_duplicates(Inv)
        load_inventory(bad_file)
    assert expected_error_snippet in str(excinfo.value).lower()


def test_valid_inventory():
    inv = load_inventory("tests/fixtures/valid_inventory.yaml")
    check_duplicates(inv)
    assert len(inv.devices) == 2


def test_invalid_role():
    with pytest.raises(ValidationError):
        load_inventory("tests/fixtures/invalid_role.yaml")

def test_duplicate_name():
    inv = load_inventory("tests/fixtures/duplicate_name.yaml")
    with pytest.raises(ValueError, match="duplicate name"):
        check_duplicates(inv)


def test_cli_success():
    result = subprocess.run(
        [sys.executable, "-m", "inventory_validator.cli",
         "tests/fixtures/valid_inventory.yaml"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "OK:" in result.stdout


def test_cli_failure():
    result = subprocess.run(
        [sys.executable, "-m", "inventory_validator.cli",
         "tests/fixtures/duplicate_ip.yaml"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 1
    assert "ERROR:" in result.stdout