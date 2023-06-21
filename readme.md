# Cannon
Canonical OpenStack Validation Suite

## Quick Start
Install the python package in editable mode in the development virtualenv
```
make dev-environment
source .venv/bin/activate
python3 -m pip install -e .
```
Run a minimal VM spin-up test
```
cannon functional run minimal
```
See help
```
cannon functional run --help
```
