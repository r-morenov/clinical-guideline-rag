"""Load page text files from a folder (a stand-in for PDF extraction until Phase 2)."""

import logging
from pathlib import Path

from clinical_guideline_rag.models import Chunk, ChunkValidationError
from clinical_guideline_rag.text_utils import join_hyphenated_line_breaks, normalize_whitespace

logger = logging.getLogger(__name__)  # a logbook named after this module


def load_page_chunks(folder: Path, guideline: str) -> list[Chunk]:
    """Turn every page_<n>.txt file in a folder into one cleaned Chunk per page."""
    if not folder.is_dir():
        raise FileNotFoundError(f"folder not found: {folder}")

    chunks: list[Chunk] = []
    for path in folder.glob("page_*.txt"):  # every file matching the pattern; * = anything
        page = int(path.stem.split("_")[1])  # "page_3.txt" -> stem "page_3" -> "3" -> 3
        raw = path.read_text(encoding="utf-8")
        text = normalize_whitespace(
            join_hyphenated_line_breaks(raw)
        )  # ORDER MATTERS: see question 2
        try:
            chunks.append(Chunk(guideline=guideline, page=page, chunk_index=0, text=text))
        except ChunkValidationError as error:
            logger.warning("Skipping %s: %s", path.name, error)

    chunks.sort(
        key=lambda chunk: chunk.page
    )  # put pages in order; lambda = a tiny one-line function
    logger.info("Loaded %d chunks from %s", len(chunks), folder)
    return chunks
