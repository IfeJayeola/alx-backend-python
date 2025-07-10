import sqlite3

class ExecuteQuery:
	def __init__(self, query, param):
		self.conn = None
		self.query = query
		self.param = param

	def __enter__(self):
		self.conn = sqlite3.connect('users.db')
		cursor = self.conn.cursor()
		return cursor.execute(self.query, self.param)

	def __exit__(self, exc_type, exc_value, exc_traceback):
		self.conn.close()

with ExecuteQuery("SELECT * FROM users WHERE age > ?", (25,)) as c:
		for row in c:
			print(row)
