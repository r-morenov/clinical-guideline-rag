"""Application settings, read from environment variables or a local .env file."""

from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Every configurable value in one place, with safe defaults for local development.

    Each field can be overridden by an environment variable with the CGR_ prefix,
    for example CGR_LLM_MODEL=qwen3:8b.
    """

    model_config = SettingsConfigDict(
        env_prefix="CGR_",  # only read variables that start with CGR_
        env_file=".env",  # also read a local .env file if it exists (never committed)
        extra="ignore",  # ignore unrelated lines in .env instead of failing
    )

    ollama_url: str = "http://localhost:11434"
    llm_model: str = "llama3.2:3b"
    embedding_model: str = "nomic-embed-text"
    data_dir: Path = Path("data")
    log_level: str = "INFO"


def get_settings() -> Settings:
    """Read the current settings from the environment."""
    return Settings()
