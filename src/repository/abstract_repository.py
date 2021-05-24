
from abc import ABCMeta, abstractmethod
from src.entities.entities import IdType, ToDoItem


class AbstractToDoItemRepository(metaclass=ABCMeta):
    # Create
    @abstractmethod
    def create(self, item: ToDoItem):
        pass

    # Read
    @abstractmethod
    def get_item_by_id(self, item_id: IdType) -> ToDoItem:
        pass

    # Update
    @abstractmethod
    def update(self, item: ToDoItem):
        pass

    # Delete
    @abstractmethod
    def delete(self, item: ToDoItem):
        pass