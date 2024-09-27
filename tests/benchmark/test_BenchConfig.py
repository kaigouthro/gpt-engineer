# Generated by CodiumAI

import pytest

from gpt_engineer.benchmark.bench_config import (
    AppsConfig,
    BenchConfig,
    GptmeConfig,
    MbppConfig,
)


class TestBenchConfig:
    #  Creating a BenchConfig object with default values should return an instance of BenchConfig with all attributes set to their default values.
    def test_default_values(self):
        config = BenchConfig()
        assert isinstance(config.apps, AppsConfig)
        assert isinstance(config.mbpp, MbppConfig)
        assert isinstance(config.gptme, GptmeConfig)
        assert config.apps.active is True
        assert config.apps.test_start_index == 0
        assert config.apps.test_end_index == 1
        assert config.apps.train_start_index == 0
        assert config.apps.train_end_index == 0
        assert config.mbpp.active is True
        assert config.mbpp.test_len == 1
        assert config.mbpp.train_len == 0
        assert config.gptme.active is True

    #  Creating a BenchConfig object with specific values should return an instance of BenchConfig with the specified attributes set to the specified values.
    def test_specific_values(self):
        config = BenchConfig(
            apps=AppsConfig(
                active=False,
                test_start_index=1,
                test_end_index=2,
                train_start_index=3,
                train_end_index=4,
            ),
            mbpp=MbppConfig(active=False, test_len=5, train_len=6),
            gptme=GptmeConfig(active=False),
        )
        assert isinstance(config.apps, AppsConfig)
        assert isinstance(config.mbpp, MbppConfig)
        assert isinstance(config.gptme, GptmeConfig)
        assert config.apps.active is False
        assert config.apps.test_start_index == 1
        assert config.apps.test_end_index == 2
        assert config.apps.train_start_index == 3
        assert config.apps.train_end_index == 4
        assert config.mbpp.active is False
        assert config.mbpp.test_len == 5
        assert config.mbpp.train_len == 6
        assert config.gptme.active is False

    #  Calling the from_dict method with a valid dictionary should return an instance of BenchConfig with attributes set according to the values in the dictionary.
    def test_from_dict_valid_dict(self):
        config_dict = {
            "apps": {
                "active": False,
                "test_start_index": 1,
                "test_end_index": 2,
                "train_start_index": 3,
                "train_end_index": 4,
            },
            "mbpp": {"active": False, "test_len": 5, "train_len": 6},
            "gptme": {"active": False},
        }
        config = BenchConfig.from_dict(config_dict)
        assert isinstance(config.apps, AppsConfig)
        assert isinstance(config.mbpp, MbppConfig)
        assert isinstance(config.gptme, GptmeConfig)
        assert config.apps.active is False
        assert config.apps.test_start_index == 1
        assert config.apps.test_end_index == 2
        assert config.apps.train_start_index == 3
        assert config.apps.train_end_index == 4
        assert config.mbpp.active is False
        assert config.mbpp.test_len == 5
        assert config.mbpp.train_len == 6
        assert config.gptme.active is False

    #  Calling the from_toml method with an invalid path to a TOML file should raise an appropriate exception.
    def test_from_toml_invalid_path(self):
        config_file = "invalid_config.toml"
        with pytest.raises(Exception):
            BenchConfig.from_toml(config_file)
