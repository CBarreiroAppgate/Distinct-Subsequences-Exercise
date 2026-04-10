# Distinct Subsequences Exercise

Solution to the **Distinct Subsequences** problem implemented with clean code principles: **Hexagonal Architecture** (Ports & Adapters), **Dynamic Programming**, and a REST API with FastAPI.

---

## Problem

Given a string `source` and a string `target`, count how many distinct subsequences of `source` equal `target`.

**Example:**
- `source = "rabbbit"`, `target = "rabbit"` → **3**

The same problem applies to event sequences (lists of strings).

---

## Requirements

- Python 3.10+
- pip

---

## Installation

```bash
# Clone the repository
git clone <repo-url>
cd Distinct-Subsequences-Exercise

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## Running the server

```bash
python -m src.app.main
```

The server starts at `http://localhost:8000`.

Interactive API documentation (Swagger UI) is available at `http://localhost:8000/docs`.

---

## API Endpoints

### `POST /subsequences`

Counts distinct subsequences in text strings.

**Request:**
```json
{
  "source": "rabbbit",
  "target": "rabbit"
}
```

**Response:**
```json
{
  "count": 3
}
```

**Validations:**
- `source` and `target` must contain only English letters (`[a-zA-Z]`).
- Length between 1 and 1000 characters.

---

### `POST /event-subsequences`

Counts distinct subsequences in event sequences (lists of strings).

**Request:**
```json
{
  "source": ["click", "view", "click", "buy", "click"],
  "target": ["click", "buy"]
}
```

**Response:**
```json
{
  "count": 3
}
```

**Validations:**
- Tokens must contain only `[A-Za-z0-9_-]` characters.
- List length between 1 and 1000 elements.

---

## Running the tests

```bash
# All tests
python -m pytest tests/

# A specific file
python -m pytest tests/test_subsequence_counter.py

# A test by name
python -m pytest tests/test_subsequence_counter.py::test_function_name

# With verbose output
python -m pytest tests/ -v
```

---

## Architecture

The project follows **Hexagonal Architecture** (Ports & Adapters):

```
src/app/
├── domain/
│   ├── services/
│   │   ├── subsequence_counter.py       # DP algorithm for strings
│   │   └── event_sequence_counter.py    # DP algorithm for events
│   └── value_objects/
│       ├── subsequence_query.py         # Value object with validation
│       └── event_sequence_query.py      # Value object with validation
├── application/
│   ├── ports/
│   │   ├── input/                       # Input interfaces (use cases)
│   │   └── output/                      # Output interfaces (repositories/services)
│   └── use_cases/
│       ├── count_subsequences.py        # Orchestrates the domain
│       └── count_event_subsequences.py
├── infrastructure/
│   ├── adapters/
│   │   └── input/
│   │       └── rest_api.py              # REST adapter (FastAPI)
│   └── app_factory.py                   # Dependency wiring
└── main.py                              # Entry point
```

**Dependency flow:**

```
rest_api.py → UseCase (port) ← use_cases.py → domain/services/
```

- **Domain:** pure business logic, no external dependencies.
- **Application:** defines ports (interfaces) and orchestrates the domain.
- **Infrastructure:** adapters to the outside world (HTTP, CLI, etc.).

---

## Algorithm

Uses **dynamic programming with a 1D array**, O(n × m) time complexity and O(m) space complexity, where `n = len(source)` and `m = len(target)`.