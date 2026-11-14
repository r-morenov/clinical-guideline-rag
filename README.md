# Guideline Navigator

A local, zero-cost platform that answers questions about public clinical guidelines for chronic kidney disease, type 2 diabetes and hypertension, citing the document and page behind every answer. In later phases, an AI agent will walk synthetic patients through the care pathway.

> **Research and education prototype.** Not medical advice and not for clinical use. All patient data is synthetic.

## Status
Phase 1 of 10: foundations and design.

## Planned stack
Python 3.12 · uv · PostgreSQL + pgvector · Ollama (local models) · FastAPI · Streamlit · LangGraph

## Development
Requirements: [uv](https://docs.astral.sh/uv/). It installs the right Python version (3.12) automatically.

```bash
uv sync          # install the exact dependencies recorded in uv.lock
uv run pytest    # run the test suite
```