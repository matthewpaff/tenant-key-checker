# Tenant Key Checker

Check composite tenant keys and same-tenant employee references in supplied records.

Uses Python 3.10+ and its standard library only. No package installation, virtual
environment, external server, Redis, Celery, or network access is required.

## Run

```console
python -m keys_tool --help
python -m keys_tool examples/sample.json
python -m keys_tool --check-fixtures fixtures/cases.jsonl
python generate_fixtures.py --count 20
python -m unittest discover -s tests -v
```

Run from this directory. The optional path defaults to `-`, which reads JSON from
stdin. Output is JSON or a fixture-check summary. Exit codes are 0 success,
1 file failure, and 2 invalid input. Examples and fixtures contain generated data.

Requires employees [{tenant,id}] and references [{tenant,employee_id}], each limited to 500 rows. Employee IDs are positive integers and unique within a tenant. Missing composite references are reported in input order. This checks supplied data; it is not an authentication or database isolation boundary.

## Learning focus

Independent concept exercise for modeled blueprint section B01. This is an independent concept exercise based on the modeled
roadmap. It makes no claim to be employer-owned or period-authentic production code.

## Structure

- `keys_tool/core.py`: validated parsing, storage, or state transitions.
- `keys_tool/cli.py`: JSON command interface.
- `keys_tool/generate_fixtures.py`: original deterministic validation cases.
- `keys_tool/fixture_check.py`: expected-output/error checks.
- `fixtures/cases.jsonl`: 34 generated cases, with explicit descriptions.
- `tests/`: independently selected boundaries and the complete corpus check.

Branches `feature/core`, `feature/cli`, `data/fixtures`, and `docs/usage` retain
snapshots; `main` contains the complete tool. Dates and provenance are also recorded
in TIMELINE.json. Many data cases share a scenario; they are not separate features.

Keep changes focused, use actual dates for new work, and add a regression test
for changed behavior. Licensed under [MIT](LICENSE).

[History and provenance](HISTORY.md).
