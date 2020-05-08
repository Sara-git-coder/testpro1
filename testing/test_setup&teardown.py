import pytest

def setup_module():
    print("这是一个set_moudle 方法")

def teardown_moudle():
    print("这是一个teardown_moudle 方法")

def setup_function():
    print("setup_function")

def teardown_function():
    print("teardown_function")

def test_login():
    print("这是一个外部的方法")

class TestDemo():
    def setup_class(self):
        print("setup_class")

    def setup_method(self):
        print("setup_method")