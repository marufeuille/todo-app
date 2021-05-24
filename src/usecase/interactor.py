from src.entities.entities import ToDoItem
from src.repository.abstract_repository import AbstractToDoItemRepository
from src.usecase.abstract_usecases import AbstractToDoItemCreateUseCase, ToDoItemCreateInputData


class ToDoItemCreateUseCase(AbstractToDoItemCreateUseCase):
    def __init__(self, todo_repo: AbstractToDoItemRepository):
        self.repo = todo_repo

    def handle(self, input_data: ToDoItemCreateInputData):
        next_id = self.repo.get_next_id()
        item = ToDoItem(
            id=next_id, title=input_data.title, description=input_data.description,
            start_date=input_data.start_date, due_date=input_data.due_date
        )
        self.repo.create(item)