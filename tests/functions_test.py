from cpp.functions import VariableFunction


class TestClass:
    def test_one(self):
        x = 'this'
        assert 'h' in x
        v = VariableFunction()

    def test_two(self):
        x = True
        assert x
