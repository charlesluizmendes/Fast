from datetime import datetime
from typing import Any

from src.domain.shared.event.event_interface import EventInterface


class AuthorCreatedEvent(EventInterface):
    """Evento disparado quando um autor é criado."""

    def __init__(self, event_date: Any, author_name: str):
        self.__data_time_occurred = datetime.now()
        self.__event_data = event_date
        self.__author_name = author_name  

    @property
    def data_time_occurred(self) -> datetime:
        return self.__data_time_occurred

    @property
    def event_data(self) -> Any:
        return self.__event_data

    @property
    def author_name(self) -> str:  
        return self.__author_name