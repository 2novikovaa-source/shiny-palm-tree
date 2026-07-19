# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is a personal learning/practice repository for Git and basic Python, not a production
application. There is no build system, package manifest (no `requirements.txt` / `pyproject.toml`),
linter config, or test suite. Don't assume standard tooling exists — check before suggesting
commands like `pytest`, `pip install -r requirements.txt`, etc.

## Layout

- [First_file.py](First_file.py), [github_file.py](github_file.py) — standalone scratch scripts, no
  interdependency.
- [connect_db.py](connect_db.py) — connects to a local PostgreSQL instance via `psycopg2` and runs a
  simple `SELECT * FROM example;` query. Connection settings (host/user/password/port) are
  hardcoded in the script.
- [connection.md](connection.md), [Just some general explonation for projec.md](Just some general explonation for projec.md) — informal notes about the project.
- `env/` — a local Python virtualenv; it's gitignored and should never be edited or committed to.

## Working in this repo

- `psycopg2` is the only external dependency in use (imported by `connect_db.py`). There's no
  manifest recording it — if adding new dependencies, consider whether a `requirements.txt` should
  be introduced.
- `connect_db.py` currently hardcodes database credentials (`localhost:5431`, user/db `postgres`).
  If you touch this file, do not commit real/production credentials — this pattern is only
  acceptable here because it targets a local/throwaway database.
- Scripts are run directly, e.g. `python connect_db.py` (with `env/` activated via
  `source env/bin/activate` if using the checked-in virtualenv).
