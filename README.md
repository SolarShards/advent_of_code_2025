**Advent Of Code 2025**

- **Description:** My solutions for Advent of Code 2025. Each day has a small solver module that exposes `read_input`, `part_one`, and `part_two` functions; `main.py` loads and runs available day modules and prints profiling information.

**Project Layout**
- `main.py`: runner that imports `day_<n>.solver` modules, contains a small `profile` helper, provides a CLI (`-d/--day`) to run a single day, and prints results with timing. `main.py` calls `part_one` and `part_two` with the input filename (string).
- `day_<n>/solver.py`: solution code for the day. Each solver should provide `read_input(filename)`, and `part_one(filename)` / `part_two(filename)` which accept the input filename (they may call `read_input` internally).
- `day_<n>/input.txt`: the input for that day.
- `day_<n>/unit_test.py`: unit tests for that day's solver (pytest compatible).

**Requirements**
- Python 3.8+ (no external dependencies).

**Usage**
- Run all available days (the runner stops when a `day_<n>.solver` module is missing):

```powershell
python main.py
```

- Run a single day's solver from the runner (example):

```powershell
python main.py -d 1
```

**Testing**
- The repository includes simple `unit_test.py` files under days that have tests. Run tests with `pytest` (recommended) or run individual test files with Python.

```powershell
pip install pytest          # optional, if not already installed
pytest -q
```

**Notes & Conventions**
- Solver modules assume integer inputs and follow the local `read_input` contract. `main.py` contains a `profile` helper and calls each day's `part_one`/`part_two` with the input filename.
- When adding new days, create a `day_<n>/solver.py` module with `read_input`, `part_one` and `part_two`, add `input.txt`, and optionally add `unit_test.py`.
