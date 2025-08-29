import pytest

from storylab.src import config


def test_missing_keys_raise_error(monkeypatch):
    for key in config.REQUIRED_KEYS:
        monkeypatch.delenv(key, raising=False)
    with pytest.raises(RuntimeError):
        config.load_config()


def test_load_config_success(monkeypatch):
    # ensure all required keys exist
    values = {
        "OPENAI_API_KEY": "openai",
        "OPENAI_MODEL_ID": "gpt-4",
        "GCP_API_KEY": "gcp",
        "GCP_MODEL_ID": "gpt",
        "TIMEZONE": "UTC",
    }
    for k, v in values.items():
        monkeypatch.setenv(k, v)

    cfg = config.load_config()
    assert cfg == values
