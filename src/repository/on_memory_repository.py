from src.entities.entities import IdType, ToDoItem
from typing import Dict
from src.repository.base_repository import BaseToDoItemRepository

class OnMemoryToDoItemRepository(BaseToDoItemRepository):
    def __init__(self):
        self.repo: Dict[IdType, ToDoItem] = {}

    def create(self, item: ToDoItem):
        if item.id in self.repo.keys():
            raise KeyError()
        self.repo[item.id] = item

    def get_item_by_id(self, item_id: IdType) -> ToDoItem:
        if item_id not in self.repo.keys():
            raise KeyError()
        return self.repo[item_id]

    def get_next_id(self) -> IdType:
        return max(self.repo.keys()) + 1

    def update(self, item: ToDoItem):
        if item.id not in self.repo.keys():
            raise KeyError()
        self.repo[item.id] = item

    def delete(self, item: ToDoItem):
        if item.id not in self.repo.keys():
            raise KeyError()
        if item != self.repo[item.id]:
            raise ValueError()
        del self.repo[item.id]