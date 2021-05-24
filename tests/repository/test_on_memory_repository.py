from datetime import datetime
import os, sys

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(os.path.abspath(__file__))), "..", ".."))
from src.repository.on_memory_repository import OnMemoryToDoItemRepository
from src.repository.abstract_repository import AbstractToDoItemRepository
from src.entities.entities import ToDoItem
import pytest

def test_on_memory_todo_repo():
    task = ToDoItem(id=1, title="test", description="test task", start_date=None, due_date=None)
    repo: AbstractToDoItemRepository = OnMemoryToDoItemRepository()
    repo.create(task)
    assert task == repo.get_item_by_id(task.id)
    task2 = ToDoItem(id=task.id, title=task.title, description=task.description, start_date=task.start_date, due_date=datetime(2021, 10, 1))
    repo.update(task2)
    assert task != repo.get_item_by_id(task.id)
    assert task2 == repo.get_item_by_id(task.id)
    repo.delete(task2)
    with pytest.raises(KeyError):
        repo.get_item_by_id(task.id)