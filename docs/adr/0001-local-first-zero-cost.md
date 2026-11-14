# ADR-0001: Local-first, zero-cost stack

- **Status:** Accepted
- **Date:** 2026-11-07

## Context
This is a portfolio project with a budget of $0. The documents and questions should never leave the machine, and the available hardware is a laptop with an 8 GB GPU.

## Decision
Run everything locally with open-source tools: Ollama for language and embedding models, PostgreSQL + pgvector in Docker, and Python managed with uv. No paid APIs and no cloud services.

## Alternatives considered
- **Hosted LLM APIs:** stronger models, but they cost money and send data to a third party.
- **Cloud vector databases:** convenient, but not free at useful scale and add an external dependency.

## Consequences
- Positive: $0 running cost, full privacy, works offline, and shows infrastructure skills.
- Negative: limited to models that fit in 8 GB of VRAM (about 7–9B parameters), which are less capable than frontier models. Answer quality must therefore be measured carefully (Phase 6).