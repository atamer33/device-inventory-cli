# device-inventory-cli

# device-inventory-cli

A small Python CLI that validates YAML network device inventories before they are used in automation workflows.

## Problem

Network automation pipelines depend on inventory files listing devices, management IPs, roles, and OS types. Bad data—missing fields, invalid IPs, unknown roles, or duplicate names/IPs—often fails late in Ansible, pySROS, or CI jobs.

This tool catches those problems early with a fast local check.

## What it validates

Each device in the inventory must have:

| Field     | Rules |
|-----------|-------|
| `name`    | Non-empty string |
| `mgmt_ip` | Valid IPv4 or IPv6 address |
| `role`    | One of: `pe`, `p`, `bng`, `rr`, `core` |
| `os`      | One of: `sros`, `srlinux`, `iosxr` |

It also checks for duplicate `name` and duplicate `mgmt_ip` values across the inventory.

## Example inventory

```yaml
devices:
  - name: pe1-lab
    mgmt_ip: 10.0.0.1
    role: pe
    os: sros
  - name: p1-lab
    mgmt_ip: 10.0.0.2
    role: p
    os: sros