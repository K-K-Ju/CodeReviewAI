from codereviewai import config

def test_settings_loaded_env():
    assert config.settings.github_api_key
    assert config.settings.openai_api_key
