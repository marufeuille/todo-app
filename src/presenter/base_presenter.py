from abc import ABCMeta, abstractmethod
from typing import Generic, TypeVar

class BaseUseCaseResponseData(metaclass=ABCMeta):
    pass

T = TypeVar('T', bound=BaseUseCaseResponseData)

class BaseRepresenter(Generic[T], metaclass=ABCMeta):
    @abstractmethod
    def run(self, response: T) -> None:
        pass