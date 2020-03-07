# coding: utf-8
__author__ = 'Sky'

import time
import pytest


@pytest.fixture(scope='class', autouse=True)
def suite_data():
    print("\n> Suite setup")
    yield
    print("> Suite teardown")


@pytest.fixture(scope='function')
def case_data():
    print("   > Case setup")
    yield time.time()
    print("\n   > Case teardown")
