# Distinct Subsequences Exercise

Solución al problema **Distinct Subsequences** implementada con buenas prácticas de código: **Arquitectura Hexagonal** (Ports & Adapters), **Dynamic Programming** y una API REST con FastAPI.

---

## Problema

Dado un string `source` y un string `target`, contar cuántas subsecuencias distintas de `source` son iguales a `target`.

**Ejemplo:**
- `source = "rabbbit"`, `target = "rabbit"` → **3**

El mismo problema aplica a secuencias de eventos (listas de strings).

---

## Requisitos

- Python 3.10+
- pip

---

## Instalación

```bash
# Clonar el repositorio
git clone <repo-url>
cd Distinct-Subsequences-Exercise

# Crear y activar entorno virtual
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

---

## Correr el servidor

```bash
python -m src.app.main
```

El servidor arranca en `http://localhost:8000`.

La documentación interactiva de la API (Swagger UI) queda disponible en `http://localhost:8000/docs`.

---

## Endpoints de la API

### `POST /subsequences`

Cuenta subsecuencias distintas en strings de texto.

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

**Validaciones:**
- `source` y `target` deben contener solo letras inglesas (`[a-zA-Z]`).
- Longitud entre 1 y 1000 caracteres.

---

### `POST /event-subsequences`

Cuenta subsecuencias distintas en secuencias de eventos (listas de strings).

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

**Validaciones:**
- Los tokens deben contener solo caracteres `[A-Za-z0-9_-]`.
- Longitud de la lista entre 1 y 1000 elementos.

---

## Correr los tests

```bash
# Todos los tests
python -m pytest tests/

# Un archivo específico
python -m pytest tests/test_subsequence_counter.py

# Un test por nombre
python -m pytest tests/test_subsequence_counter.py::test_function_name

# Con detalle
python -m pytest tests/ -v
```

---

## Arquitectura

El proyecto sigue **Arquitectura Hexagonal** (Ports & Adapters):

```
src/app/
├── domain/
│   ├── services/
│   │   ├── subsequence_counter.py       # Algoritmo DP para strings
│   │   └── event_sequence_counter.py    # Algoritmo DP para eventos
│   └── value_objects/
│       ├── subsequence_query.py         # Value object con validación
│       └── event_sequence_query.py      # Value object con validación
├── application/
│   ├── ports/
│   │   ├── input/                       # Interfaces de entrada (use cases)
│   │   └── output/                      # Interfaces de salida (repositorios/servicios)
│   └── use_cases/
│       ├── count_subsequences.py        # Orquesta el dominio
│       └── count_event_subsequences.py
├── infrastructure/
│   ├── adapters/
│   │   └── input/
│   │       └── rest_api.py              # Adaptador REST (FastAPI)
│   └── app_factory.py                   # Wiring de dependencias
└── main.py                              # Punto de entrada
```

**Flujo de dependencias:**

```
rest_api.py → UseCase (port) ← use_cases.py → domain/services/
```

- **Domain:** lógica pura, sin dependencias externas.
- **Application:** define los puertos (interfaces) y orquesta el dominio.
- **Infrastructure:** adaptadores al mundo exterior (HTTP, CLI, etc.).

---

## Algoritmo

Se usa **programación dinámica con un array 1D** de complejidad O(n × m) en tiempo y O(m) en espacio, donde `n = len(source)` y `m = len(target)`.
