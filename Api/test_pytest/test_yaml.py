import pytest
import yaml


class TestDemo:
    @pytest.mark.parametrize("env", yaml.safe_load(open("./env.yml", encoding="UTF-8")))
    def test_env(self, env):
        if "test" in env:
            print("测试环境的ip是", env["test"])
        elif "dev" in env:
            print("开发环境的ip是", env["dev"])

    # [['name', 'mobile'], ['name', 'mobile1']]
    @pytest.mark.parametrize("name, mobile", yaml.safe_load(open("./data.yml", encoding="UTF-8")))
    def test_login(self, name, mobile):
        print(name, mobile)
