"""Tests for the Chunk model."""

import dataclasses

import pytest

from clinical_guideline_rag.models import Chunk, ChunkValidationError


def test_citation_shows_guideline_and_page() -> None:
    chunk = Chunk(guideline="va-dod-ckd-2025", page=12, chunk_index=0, text="Some text.")
    assert chunk.citation == "va-dod-ckd-2025, p. 12"


def test_word_count() -> None:
    chunk = Chunk(guideline="sample", page=1, chunk_index=0, text="Measure the ratio once a year.")
    assert chunk.word_count == 6


@pytest.mark.parametrize(
    ("page", "chunk_index", "text"),
    [
        (0, 0, "Some text."),  # page must start at 1
        (1, -1, "Some text."),  # chunk_index must start at 0
        (1, 0, "   "),  # text must not be empty
    ],
)
def test_invalid_chunks_are_rejected(page: int, chunk_index: int, text: str) -> None:
    with pytest.raises(ChunkValidationError):  # the test PASSES only if this error is raised
        Chunk(guideline="sample", page=page, chunk_index=chunk_index, text=text)


def test_chunk_is_frozen() -> None:
    chunk = Chunk(guideline="sample", page=1, chunk_index=0, text="Some text.")
    with pytest.raises(dataclasses.FrozenInstanceError):
        chunk.page = 5  # type: ignore  (tells VS Code we're breaking the rule on purpose)
