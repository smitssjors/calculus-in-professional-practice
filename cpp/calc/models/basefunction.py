from abc import ABC, abstractmethod


class BaseFunction(ABC):

    @abstractmethod
    def toString(self):
        return 'Base Class'

    @abstractmethod
    def evaluate(self, num):
        pass
