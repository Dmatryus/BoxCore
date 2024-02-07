from abc import ABC, abstractmethod
from typing import Iterable

class Executor(ABC):
    pass

    @abstractmethod
    def execute(self, data):
        pass

class Pipeline(Executor):

    def __init__(self, executors: Iterable[Executor]):
        self.executors = executors

    def execute(self, data):
        for executor in self.executors:
            executor.execute(data)