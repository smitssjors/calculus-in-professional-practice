from . import BaseFunction


class VariableFunction(BaseFunction):
    def toString(self):
        return 'x'

    def evaluate(self, num):
        return num
