# content of test_sample.py
class TestDemo():
    def test_one(self):
        print("开始执行test_one方法")
        x = "this"
        assert "h" in x

    def test_two(self):
        print("开始执行test_two方法")
        x = "hello"
        assert "h" in x

    def test_three(self):
        print("开始执行test_three方法")
        x = "hello"
        y = "hello world"
        assert x  not in y

class TestDemo1():
    def test_a(self):
        print("开始执行test_a方法")
        x = "this"
        assert "h" in x

    def test_b(self):
        print("开始执行test_b方法")
        x = "hello"
        assert "h" in x

    def test_c(self):
        print("开始执行test_c方法")
        x = "hello"
        y = "hello world"
        assert x not in y