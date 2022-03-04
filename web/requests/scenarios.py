import os
from typing import List, Optional

from flask import current_app

from database import select_from_db
from database import SQLProvider


class StudentsInGroupScenario:

	def __init__(self, group: str) -> None:
		self.db_config = current_app.config['DB_CONFIG']
		self.provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))

		if not group or not isinstance(group, str):
			raise ValueError('Group is invalid')
		self.group = group

	def execute(self) -> List[dict]:
		result = []
		sql_params = {'group_index': self.group}
		sql_code = self.provider.get('students_in_group.sql', params=sql_params)
		for student in select_from_db(sql_code, self.db_config):
			result.append(student)
		return result


class StudentExamResultScenario:

	def __init__(self, first_name: str, last_name: str, code: str) -> None:
		self.db_config = current_app.config['DB_CONFIG']
		self.provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))
		student = self._find_student(first_name, last_name, code)
		if student is None:
			raise ValueError('No such student')
		self.student = student

	def _find_student(self, first_name: str, last_name: str, code: str) -> Optional[dict]:
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
		return student_dict

	def execute(self) -> List[dict]:
		sql_params = {'code': self.student['code']}
		sql_code = self.provider.get('students_exam_results.sql', params=sql_params)

		result = []
		for exam_result in select_from_db(sql_code, self.db_config):
			result.append(exam_result)
		return result
