# coding: utf-8
__author__ = 'Sky'

class TestSuite():

    def test_case_1(self, case_data):
        time = int(case_data)
        print("      > Received from fixture timestamp is: {}".format(time))
        assert(time % 2 == 0)

# terminal
# (venv20200219_pytest) F:\VikProject\pytest\20200219_vikpy>pytest -v -s test_test.py
# или только для одного теста из кучи
# pytest -v -s test_test.py::TestSuite::test_case_1

# https://medium.com/@dmrlx/%D0%B2%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B2-pytest-cc6175c7d0dc
# https://medium.com/@dmrlx/%D0%BF%D0%B5%D1%80%D0%B5%D0%B4%D0%B0%D1%87%D0%B0-%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D0%BE%D0%B2-%D0%BA%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4%D0%BD%D0%BE%D0%B9-%D1%81%D1%82%D1%80%D0%BE%D0%BA%D0%B8-%D0%B2-pytest-412e4201d085
# https://habr.com/ru/company/yandex/blog/242795/

# https://docs.pytest.org/en/latest/contents.html

