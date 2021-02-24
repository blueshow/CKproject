import sys
import pytest
import yaml

sys.path.append('..')
from pythoncode.Calculator import Calculator


def get_datas(name, type='int'):
    with open("./datas/calc.yml") as f:
        data_all = yaml.safe_load(f)
    print(data_all)
    datas = data_all[name][type]['datas']
    ids = data_all[name][type]['ids']
    return (datas, ids)


@pytest.fixture()
def get_instance():
    print("开始计算")
    calc: Calculator = Calculator()
    yield calc
    print("结束计算")


@pytest.fixture(params=get_datas('add', 'int')[0], ids=get_datas('add', 'int')[1])
def get_adddatas_with_fixture(request):
    return request.param


@pytest.fixture(params=get_datas('div', 'int')[0], ids=get_datas('div', 'int')[1])
def get_divdatas_with_fixture(request):
    return request.param
