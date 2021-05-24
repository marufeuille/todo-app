from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class ToDoItemCreateInputData:
    title: str
    description: Optional[str]
    start_date: Optional[datetime]
    due_date: Optional[datetime]

class AbstractToDoItemCreateUseCase(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, input_data: ToDoItemCreateInputData):
        pass

@dataclass
class CalculateDueDateInputData:
    due: datetime
    include: bool = True

class AbstractCalculateDueDateUseCase(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, input_data: CalculateDueDateInputData):
        pass