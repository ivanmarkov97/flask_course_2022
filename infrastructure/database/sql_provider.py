import os

from string import Template


class SQLProvider:

	def __init__(self, file_path: str) -> None:
		self._scripts = {}

		for file in os.listdir(file_path):
			self._scripts[file] = Template(open(f'{file_path}/{file}').read())

	def get(self, name: str, params: dict) -> str:
		template = self._scripts.get(name, None)
		if template is None:
			raise ValueError(f'No such template {name}')
		sql_code = template.substitute(**params)
		return sql_code
