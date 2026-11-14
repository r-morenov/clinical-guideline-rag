"""Tests for the text cleaning helpers."""

import pytest

from clinical_guideline_rag.text_utils import (
    count_words,
    join_hyphenated_line_breaks,
    normalize_whitespace,
)


@pytest.mark.parametrize(
    ("raw", "expected"),                                    # the names of the two columns of the table
    [
        ("  Chronic   kidney\n\ndisease ", "Chronic kidney disease"),
        ("tab\tseparated", "tab separated"),                # \t is a tab character
        ("", ""),                                           # edge case: empty text
        ("already clean", "already clean"),                 # edge case: nothing to fix
    ],
)
def test_normalize_whitespace(raw: str, expected: str) -> None:
    assert normalize_whitespace(raw) == expected


def test_count_words_ignores_extra_whitespace() -> None:
    assert count_words("  Chronic   kidney\n\ndisease ") == 3


def test_count_words_of_empty_text_is_zero() -> None:
    assert count_words("") == 0


def test_rejoins_word_split_across_lines() -> None:
    assert join_hyphenated_line_breaks("chronic kid-\nney disease") == "chronic kidney disease"


def test_keeps_hyphen_inside_a_line() -> None:
    assert join_hyphenated_line_breaks("follow-up visit") == "follow-up visit"


@pytest.mark.xfail(reason="known limitation: a real hyphen at a line break is lost")
def test_keeps_real_hyphen_at_line_break() -> None:
    assert join_hyphenated_line_breaks("follow-\nup visit") == "follow-up visit"