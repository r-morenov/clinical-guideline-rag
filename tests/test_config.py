"""Tests for the settings."""

import pytest

from clinical_guideline_rag.config import Settings


def test_defaults_point_to_local_services(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("CGR_OLLAMA_URL", raising=False)  # remove the variable for this test only
    settings = Settings(_env_file=None)  # _env_file=None: ignore any local .env
    assert settings.ollama_url == "http://localhost:11434"


def test_environment_variable_overrides_default(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("CGR_LLM_MODEL", "qwen3:8b")  # set a variable for this test only
    settings = Settings(_env_file=None)
    assert settings.llm_model == "qwen3:8b"
