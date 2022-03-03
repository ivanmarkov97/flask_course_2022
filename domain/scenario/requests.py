import abc
from typing import List

from domain.entity import Student, Group
from domain.entity import StudentInGroupEntity
from domain.entity import StudentExamResultsEntity


class StudentsInGroupScenario(abc.ABC):

	def __init__(self, group: Group) -> None:
		self.group = group

	@abc.abstractmethod
	def execute(self) -> List[StudentInGroupEntity]:
		raise NotImplementedError


class StudentExamResultScenario(abc.ABC):

	def __init__(self, student: Student) -> None:
		self.student = student

	@abc.abstractmethod
	def execute(self) -> List[StudentExamResultsEntity]:
		raise NotImplementedError
