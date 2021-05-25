from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from src.entities.entities import IdType, ToDoItem
from src.repository.base_repository import BaseToDoItemRepository
from src.usecase.base_usecases import BaseUseCase, BaseUseCaseRequestData

@dataclass
class CreateTodoRequestData(BaseUseCaseRequestData):
    title: str
    description: Optional[str]
    start_date: Optional[datetime]
    due_date: Optional[datetime]

class CreateTodoItemInteractor(BaseUseCase):
    def __init__(self, todo_repo: BaseToDoItemRepository):
        self.repo = todo_repo

    def execute(self, request: CreateTodoRequestData):
        next_id = self.repo.get_next_id()
        item = ToDoItem(
            id=next_id, title=request.title, description=request.description,
            start_date=request.start_date, due_date=request.due_date
        )
        self.repo.create(item)

@dataclass
class FinishToDoRequestData(BaseUseCaseRequestData):
    id: IdType

class FinishTodoItemInteractor(BaseUseCase):
    def __init__(self, todo_repo: BaseToDoItemRepository):
        self.repo = todo_repo

    def execute(self, request: FinishToDoRequestData) -> None:
        todo = self.repo.get_item_by_id(request.id)
        todo.finished = True
        self.repo.update(todo)