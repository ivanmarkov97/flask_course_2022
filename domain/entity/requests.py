from dataclasses import dataclass
from .base import Student, Group, Subject


@dataclass
class StudentInGroupEntity:
	student: Student
	group: Group


@dataclass
class StudentExamResultsEntity:
	student: Student
	exam: Subject
	mark: int
