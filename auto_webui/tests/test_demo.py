import unittest

import pytest






data = [1,2,3]


@pytest.fixture(scope="function")
def function_fixture():
    print("function before")
    yield
    print("function after")


@pytest.fixture(scope="class")
def class_fixture():
    print("class before")
    yield
    print("class after")


@pytest.fixture(scope="module")
def module_fixture():
    print("module before")
    yield
    print("module after")


@pytest.mark.demo
class TestDemo():

    @pytest.mark.smoke
    @pytest.mark.error_test
    # 实现参数化
    # @pytest.mark.parametrize("test_info", data)
    def test_demo_no_class(self,
                           # test_info,
                           # function_fixture,
                           # class_fixture,
                           # module_fixture
                           ):
        assert  1 == 2



    def test_demo_success(self,
                          function_fixture,
                          class_fixture,
                          module_fixture
                          ):
        pass



def test_demo_error(module_fixture, class_fixture):
    print("value")
    assert 1 == 2

def test_demo_success(module_fixture, class_fixture):
    pass