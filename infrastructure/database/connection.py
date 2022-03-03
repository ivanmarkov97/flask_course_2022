from typing import Optional, Any, NewType

from pymysql import connect
from pymysql.connections import Cursor
from pymysql.connections import Connection
from pymysql.err import OperationalError

O_Cursor = NewType('O_Cursor', Optional[Cursor])
O_Connection = NewType('O_Connection', Optional[Connection])


class DBConnection:

	def __init__(self, config: dict) -> None:
		self.config: dict = config
		self.cursor: O_Cursor = None
		self.connection: O_Connection = None

	def __enter__(self) -> O_Cursor:
		try:
			self.connection = connect(**self.config)
			self.cursor = self.connection.cursor()
			# start transaction block
			self.connection.begin()
			return self.cursor
		except OperationalError:
			return None

	def __exit__(self, exc_type: Optional[Any], exc_val: Optional[Any], exc_tb: Optional[Any]) -> bool:
		if self.connection is not None and self.cursor is not None:
			# end transaction block
			if exc_type is not None:
				self.connection.rollback()
			else:
				self.connection.commit()
			self.cursor.close()
			self.connection.close()
			return True
		return False


if __name__ == '__main__':
	test_config = {
		'host': '127.0.0.1',
		'port': 3306,
		'user': 'root',
		'password': 'root',
		'db': 'joom'
	}

	with DBConnection(test_config) as cursor:
		cursor.execute('select version()')
		print(cursor.fetchone())
