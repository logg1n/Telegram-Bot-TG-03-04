# models.py
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    grade = Column(String(20), nullable=False)

    def __repr__(self):
        return f"<Student(name='{self.name}', age={self.age}, grade='{self.grade}')>"
