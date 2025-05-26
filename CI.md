# Continuous Integration (CI) for Tree of Life Cladogram

## Recommended CI: GitHub Actions

- Run backend Python tests and frontend JS tests on every push/PR.

Example `.github/workflows/ci.yml`:

```yaml
name: CI

on: [push, pull_request]

jobs:
  backend:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.11"
      - name: Install dependencies
        run: |
          cd scripts
          pip install -r requirements.txt
      - name: Run backend tests
        run: |
          cd scripts
          python -m unittest discover

  frontend:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Node.js
        uses: actions/setup-node@v3
        with:
          node-version: "20"
      - name: Install dependencies and run tests
        run: |
          cd web
          npm install
          npm test
```
- Adapt as needed for your repo and preferred test runners.