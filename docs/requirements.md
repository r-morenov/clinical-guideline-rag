# Requirements

Guideline Navigator (repository: clinical-guideline-rag) answers questions about public clinical guidelines for chronic kidney disease, type 2 diabetes and hypertension, citing the source of every answer.

> Research and education prototype. Not medical advice and not for clinical use. All patient data is synthetic.

## Users and main use cases

| ID | User | Use case |
| --- | --- | --- |
| UC-1 | Learner or reviewer | Asks a question about a guideline recommendation and gets an answer with the guideline and page it comes from |
| UC-2 | Maintainer | Adds a new guideline PDF and makes it searchable with one command |
| UC-3 | Evaluator | Runs a fixed question set and gets quality and speed metrics (Phase 6) |
| UC-4 | Learner or reviewer | Compares what two guidelines say on the same topic (Phase 7) |
| UC-5 | Clinician role (simulated) | Reviews and approves a cited care-pathway summary for a synthetic patient (Phase 7) |

## Functional requirements

| ID | Requirement | Priority |
| --- | --- | --- |
| FR-1 | Ingest the guideline PDFs listed in a manifest with one command | Must |
| FR-2 | Extract text page by page, keeping page numbers | Must |
| FR-3 | Clean the text: whitespace, broken hyphenation, repeated headers and footers | Must |
| FR-4 | Split text into chunks that carry guideline, version year, page and position | Must |
| FR-5 | Embed chunks with a local model and store them with their metadata in PostgreSQL + pgvector | Must |
| FR-6 | Answer a natural-language question using retrieved chunks and a local LLM | Must |
| FR-7 | Cite the guideline and page for the passages that support each answer | Must |
| FR-8 | Say the documents do not cover a question instead of guessing | Must |
| FR-9 | Show the research-and-education disclaimer with every answer | Must |
| FR-10 | Log every query: question, retrieved chunk IDs, model, latency and answer | Must |
| FR-11 | Offer ingestion and question answering through a REST API and a simple demo UI | Must |
| FR-12 | Evaluate retrieval and answers on a fixed question set with one command | Later (Phase 6) |
| FR-13 | Agent drafts a cited care-pathway summary for a synthetic patient, flags differences between guidelines, and waits for human approval | Later (Phase 7) |

## Non-functional requirements

| ID | Requirement |
| --- | --- |
| NFR-1 | **Cost:** $0. Open-source tools and local models only; no paid APIs or cloud services |
| NFR-2 | **Privacy:** runs fully on one laptop; no document or question leaves the machine; only public documents and synthetic patient data |
| NFR-3 | **Hardware:** runs on a laptop with 8 GB of VRAM and 32 GB of RAM, with the language model fully on the GPU |
| NFR-4 | **Speed:** initial target of under 10 seconds for a typical answer (median), to be measured in Phase 4 and revised with data |
| NFR-5 | **Reproducibility:** the environment rebuilds exactly from `uv.lock`; the full stack starts with one command (Phase 8) |
| NFR-6 | **Quality:** automated tests for the core logic; linting; tests run on every pull request (Phase 8) |
| NFR-7 | **Traceability:** every answer can be traced to its source chunks and the model version that produced it |
| NFR-8 | **Licensing:** guideline PDFs are never redistributed; a manifest records each source and its licence |
| NFR-9 | **Safety:** outputs are never presented as recommendations for real patients; the system refuses when evidence is missing |

## Out of scope
- Scanned PDFs that need OCR, and extraction of images or complex tables
- User accounts, authentication, multiple users
- Cloud deployment and model fine-tuning
- Real patient data or any confidential document
- Languages other than English (Spanish sources are a possible later extension)