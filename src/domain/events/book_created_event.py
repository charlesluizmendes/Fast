from datetime import datetime
from typing import Any

from src.domain.shared.event.event_interface import EventInterface


class BookCreatedEvent(EventInterface):
    """Evento disparado quando um livro é criado."""

    def __init__(self, event_date: Any, title: str, author_id: str):
        self.__data_time_occurred = datetime.now()
        self.__event_data = event_date
        self.title = title
        self.author_id = author_id

    def data_time_occurred(self) -> datetime:
        return self.__data_time_occurred

    def event_data(self) -> Any:
        return self.__event_data