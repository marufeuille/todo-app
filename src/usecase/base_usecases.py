from abc import ABCMeta, abstractmethod
from typing import Generic, TypeVar


class BaseUseCaseRequestData(metaclass=ABCMeta):
    pass

T = TypeVar('T', bound=BaseUseCaseRequestData)

class BaseUseCase(Generic[T], metaclass=ABCMeta):
    @abstractmethod
    def execute(self, request: T) -> None:
        pass

