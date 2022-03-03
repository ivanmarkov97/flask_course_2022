from typing import List

from .connection import DBConnection


def select_from_db(sql: str, config: dict) -> List[dict]:
	result = []
	with DBConnection(config) as cursor:
		cursor.execute(sql)
		schema = [c[0] for c in cursor.description]

		for row in cursor.fetchall():
			result.append(dict(zip(schema, row)))
		return result


def insert_into_db(sql: str, config: dict) -> int:
	with DBConnection(config) as cursor:
		result = cursor.execute(sql)
	return result
