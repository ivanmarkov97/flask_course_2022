import os
from typing import List, Optional

from flask import current_app

from domain.entity import Student, Group
from domain.entity import StudentInGroupEntity
from domain.scenario import StudentsInGroupScenario
from domain.scenario import StudentExamResultScenario

from infrastructure.database import select_from_db
from infrastructure.database import SQLProvider


class StudentsInGroupScenarioAdapter(StudentsInGroupScenario):

	def __init__(self, group: str) -> None:
		self.db_config = current_app.config['DB_CONFIG']
		self.provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))

		if not group or not isinstance(group, str):
			raise ValueError('Group is invalid')
		group_entity = Group(name=group)
		super().__init__(group=group_entity)

	def execute(self) -> List[StudentInGroupEntity]:
		result = []
		sql_params = {'group_index': self.group.name}
		sql_code = self.provider.get('students_in_group.sql', params=sql_params)
		for student in select_from_db(sql_code, self.db_config):
			result.append(StudentInGroupEntity(**student))
		return result


class StudentExamResultScenarioAdapter(StudentExamResultScenario):

	def __init__(self, first_name: str, last_name: str, code: str) -> None:
		self.db_config = current_app.config['DB_CONFIG']
		self.provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))
		student = self._find_student(first_name, last_name, code)
		if student is None:
			raise ValueError('No such student')
		super().__init__(student=student)

	def _find_student(self, first_name: str, last_name: str, code: str) -> Optional[Student]:
		search_params = {
			'first_name': first_name,
			'last_name': last_name,
			'code': code
		}
		sql_code = self.provider.get('get_student.sql', params=search_params)
		result = select_from_db(sql_code, self.db_config)
		if not result:
			return None
		student_dict = result[0]
		return Student(**student_dict)

	def execute(self) -> List[StudentInGroupEntity]:
		sql_params = {'code': self.student.code}
		sql_code = self.provider.get('students_in_group.sql', params=sql_params)

		result = []
		for student in select_from_db(sql_code, db_config):
			result.append(StudentInGroupEntity(**student))
		return result
