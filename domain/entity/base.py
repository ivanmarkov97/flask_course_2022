from dataclasses import dataclass
from datetime import datetime


@dataclass
class Group:
	name: str


@dataclass
class Student:
	first_name: str
	last_name: str
	birth_date: datetime
	code: str


@dataclass
class Subject:
	name: str
