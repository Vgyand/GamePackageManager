
from abc import ABC, abstractmethod


class DB_Manipulator(ABC):
    @abstractmethod
    def __init__(self, passed_session):
        self.session = passed_session
    pass

    @abstractmethod
    def select(self):
        pass

    @abstractmethod
    def insert(self):
        pass

    @abstractmethod
    def delete(self):
        pass
