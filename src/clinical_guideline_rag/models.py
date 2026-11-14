"""Data structures shared across the pipeline."""

from dataclasses import dataclass

from clinical_guideline_rag.text_utils import count_words


class ChunkValidationError(ValueError):
    """Raised when a chunk is created with impossible data."""


@dataclass(frozen=True)
class Chunk:
    """A piece of guideline text, together with where it came from."""

    guideline: str  # short id of the source document, e.g. "va-dod-ckd-2025"
    page: int  # page number in the PDF, starting at 1
    chunk_index: int  # position of this chunk within its page, starting at 0
    text: str  # the cleaned text itself

    def __post_init__(self) -> None:
        """Check the fields right after the chunk is created."""
        if self.page < 1:
            raise ChunkValidationError(f"page must be 1 or higher, got {self.page}")
        if self.chunk_index < 0:
            raise ChunkValidationError(f"chunk_index must be 0 or higher, got {self.chunk_index}")
        if not self.text.strip():
            raise ChunkValidationError("text must not be empty")

    @property
    def word_count(self) -> int:
        """Number of words in the chunk (reuses the Unit 2 helper)."""
        return count_words(self.text)

    @property
    def citation(self) -> str:
        """Human-readable source reference, e.g. 'va-dod-ckd-2025, p. 12'."""
        return f"{self.guideline}, p. {self.page}"
