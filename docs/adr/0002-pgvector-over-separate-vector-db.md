# ADR-0002: pgvector in PostgreSQL instead of a separate vector database

- **Status:** Accepted
- **Date:** 2026-11-07

## Context
Each chunk needs both metadata (guideline, page) and an embedding vector. Queries must filter by metadata, and later combine keyword search with vector search (hybrid retrieval). The corpus is small: thousands of chunks, not millions.

## Decision
Store metadata and vectors together in PostgreSQL, using the pgvector extension.

## Alternatives considered
- **Chroma:** simple to start with, but it becomes a second data store that must stay in sync with the metadata.
- **FAISS:** a fast search library, but no built-in persistence or metadata filtering.
- **Dedicated vector databases (Qdrant, Weaviate):** powerful, but more infrastructure than this scale needs.

## Consequences
- Positive: one database; metadata filters and vector search in a single SQL query; full-text search built in for hybrid retrieval; a stack widely used in industry.
- Negative: requires learning SQL and schema migrations. At very large scale a specialised vector database could be faster, which is not relevant here.