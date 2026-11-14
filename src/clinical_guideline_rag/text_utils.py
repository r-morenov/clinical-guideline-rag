"""Small helpers for cleaning text extracted from PDF guidelines."""


def normalize_whitespace(text: str) -> str:
    """Collapse every run of spaces, tabs and line breaks into one space.

    Example: "  Chronic   kidney\n\ndisease " -> "Chronic kidney disease"
    """
    words = text.split()  # split on ANY whitespace and drop the empty pieces
    return " ".join(words)  # glue the pieces back together with exactly one space between them


def count_words(text: str) -> int:
    """Return how many words the text contains.

    Example: "Chronic kidney disease" -> 3
    """
    return len(text.split())  # split into a list of words, then count the items in that list


def join_hyphenated_line_breaks(text: str) -> str:
    """Rejoin words that a PDF split across two lines with a hyphen.

    Example: "chronic kid-\nney disease" -> "chronic kidney disease"
    """
    return text.replace(
        "-\n", ""
    )  # delete every "hyphen + line break" pair, so "kid-\nney" becomes "kidney"
