#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

export PYTHONPATH="${ROOT}/src"

python -m inventory_validator.cli "${1:-tests/fixtures/valid_inventory.yaml}"