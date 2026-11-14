# ADR-0003: Develop inside WSL2

- **Status:** Accepted
- **Date:** 2026-11-07

## Context
The development machine runs Windows 11, but most AI and backend tooling (Docker, Ollama, Python libraries with native builds) is Linux-first, and production servers and CI pipelines run Linux.

## Decision
Do all development inside WSL2 with Ubuntu. Code lives in the Linux filesystem (`~/projects`), and Ollama runs inside WSL2.

## Alternatives considered
- **Native Windows:** easier on day one, but more path, permission and tooling problems later.
- **Dual boot or a full virtual machine:** a real Linux environment, but heavier to run day to day.

## Consequences
- Positive: the same operating system as production and CI, fewer environment problems, and Linux skills.
- Negative: an extra layer to understand: Windows–Linux interoperability, Docker Desktop integration, and GPU memory shared with Windows applications.