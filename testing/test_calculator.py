# content of test_sample.py
import allure


@allure.feature("计算器")
class TestCalc:
    # add_int_data = get_datas('add', 'int')
    # div_int_data = get_datas('div', 'int')
    @allure.title("相加_{get_adddatas_with_fixture[0]}")
    @allure.story("相加功能")
    def test_add(self, get_instance, get_adddatas_with_fixture):
        f = get_adddatas_with_fixture
        assert f[2] == round(get_instance.add(f[1], f[0]), 2)

    # @pytest.mark.parametrize("a,b,result", add_int_data[0], ids=add_int_data[1])
    # def test_add(self, get_instance, a, b, result):
    #     assert result == round(get_instance.add(a, b), 2)
    @allure.title("相减_{get_divdatas_with_fixture[0]}")
    @allure.story("相除功能")
    def test_div(self, get_instance, get_divdatas_with_fixture):
        f = get_divdatas_with_fixture
        if f[1] != 0:
            assert round(f[2], 2) == round(get_instance.div(f[0], f[1]), 2)
        else:
            try:
                get_instance.div(f[0], f[1])
            except Exception as e:
                print(e)

    # @pytest.mark.parametrize("a,b,result", div_int_data[0], ids=div_int_data[1])
    # def test_div(self, get_instance, a, b, result):
    #     if b != 0:
    #        assert round(result,  2) == round(get_instance.div(a, b),  2)
    #     else:
    #         try:
    #             get_instance.div(a, b)
    #         except Exception as e:
    #             print(e)
