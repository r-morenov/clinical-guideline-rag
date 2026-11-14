"""Tests for the page loader."""

from pathlib import Path

import pytest

from clinical_guideline_rag.loading import load_page_chunks

FIXTURES = Path(__file__).parent / "fixtures" / "sample_guideline"  # the folder next to this test file


def test_loads_valid_pages_in_order() -> None:
    chunks = load_page_chunks(FIXTURES, guideline="sample")
    assert [chunk.page for chunk in chunks] == [1, 2]       # page 3 (empty) was skipped


def test_cleans_text_while_loading() -> None:
    chunks = load_page_chunks(FIXTURES, guideline="sample")
    assert "kidney damage" in chunks[0].text                # "kid-\nney" was rejoined


def test_empty_page_is_logged(caplog: pytest.LogCaptureFixture) -> None:
    load_page_chunks(FIXTURES, guideline="sample")
    assert "Skipping page_3.txt" in caplog.text             # caplog captures the log messages


def test_missing_folder_raises(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError):
        load_page_chunks(tmp_path / "does-not-exist", guideline="sample")


def test_pages_are_sorted_as_numbers(tmp_path: Path) -> None:
    (tmp_path / "page_10.txt").write_text("Tenth page.", encoding="utf-8")
    (tmp_path / "page_2.txt").write_text("Second page.", encoding="utf-8")
    chunks = load_page_chunks(tmp_path, guideline="sample")
    assert [chunk.page for chunk in chunks] == [2, 10]       # as TEXT, "10" would come before "2"