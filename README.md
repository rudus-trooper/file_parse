# File Processing Platform

Processes CSV, JSON, and XML files — validates content, parses it, and returns the record count.

## Setup

```bash
python3.13 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python -m src.main
```

## Running Tests

```bash
python -m pytest tests/
```

---

## Design Decisions (In Progress)

### Architecture

Using a **Strategy + Factory** pattern combo so new file formats can be added without rewriting existing code.

### Exception Handling

Custom exception hierarchy with manual error codes:

| Exception | Error Code | Example Message |
|---|---|---|
| `UnsupportedFileTypeError` | 1 | `"Unsupported file type: yaml"` |
| `MalformedContentError` | 2 | `"Invalid JSON"` |
| `EmptyContentError` | 3 | `"File content cannot be empty"` |

### Design Patterns (Planned)

- **Strategy Pattern** — each file format gets its own processor class with a uniform `process()` interface
- **Factory Pattern** — a factory maps file type strings to processor instances
- **Registry Pattern** — exception classes auto-register with incrementing error codes

---

## Flow Diagram

(To be added.)
