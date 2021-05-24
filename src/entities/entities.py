from dataclasses import dataclass
from datetime import datetime
from typing import Optional

IdType = int

@dataclass
class ToDoItem:
    id: IdType
    title: str
    description: Optional[str]
    start_date: Optional[datetime]
    due_date: Optional[datetime]
    finished: bool = False