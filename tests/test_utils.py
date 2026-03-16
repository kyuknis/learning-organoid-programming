import os
import pytest
from pathlib import Path
from src.utils import get_env, load_env, ROOT, DATA_DIR, ASSETS_DIR


class TestPaths:
    def test_root_is_project_root(self):
        assert (ROOT / "pyproject.toml").exists()

    def test_data_dir_exists(self):
        assert DATA_DIR.exists()

    def test_assets_dir_exists(self):
        assert ASSETS_DIR.exists()

    def test_dirs_are_under_root(self):
        assert DATA_DIR.parent == ROOT
        assert ASSETS_DIR.parent == ROOT


class TestGetEnv:
    def test_returns_value_when_set(self, monkeypatch):
        monkeypatch.setenv("CL_TEST_KEY", "abc123")
        assert get_env("CL_TEST_KEY") == "abc123"

    def test_raises_when_required_and_missing(self, monkeypatch):
        monkeypatch.delenv("CL_MISSING_KEY", raising=False)
        with pytest.raises(EnvironmentError, match="CL_MISSING_KEY"):
            get_env("CL_MISSING_KEY", required=True)

    def test_returns_empty_string_when_optional_and_missing(self, monkeypatch):
        monkeypatch.delenv("CL_MISSING_KEY", raising=False)
        assert get_env("CL_MISSING_KEY", required=False) == ""

    def test_error_message_mentions_env_example(self, monkeypatch):
        monkeypatch.delenv("CL_MISSING_KEY", raising=False)
        with pytest.raises(EnvironmentError, match=".env.example"):
            get_env("CL_MISSING_KEY")


class TestLoadEnv:
    def test_load_env_does_not_raise_when_no_dotenv_file(self):
        # load_dotenv is a no-op if .env doesn't exist — should not raise
        load_env()
