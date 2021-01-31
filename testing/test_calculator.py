# content of test_sample.py
import sys

import pytest
import yaml

sys.path.append('..')
from pythoncode.Calculator import Calculator


def get_datas():
    with open("./datas/calc.yml") as f:
        datas = yaml.safe_load(f)
    return datas


class TestCalc:
    def setup(self):
        print("开始计算")
        self.calc = Calculator()

    @pytest.mark.parametrize("a,b,result", get_datas()['add']['datas'])
    def test_add(self, a, b, result):
        assert result == self.calc.add(a, b)

    @pytest.mark.parametrize("a,b,result", get_datas()['div']['datas'])
    def test_div(self, a, b, result):
        assert result == self.calc.div(a, b)

    def teardown(self):
        print('结束计算')
