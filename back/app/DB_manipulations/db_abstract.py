from .db import Pack
from sqlalchemy import BigInteger, Boolean, Column, \
    ForeignKey, Integer, String, Enum, Float, \
    UniqueConstraint, and_, func, Date, DateTime, desc
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
