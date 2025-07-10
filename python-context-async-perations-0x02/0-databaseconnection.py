import sqlite3

class DatabaseConnection:
	def __init__(self):
		self.conn = None

	def __enter__(self):
		self.conn = sqlite3.connect('users.db')
		return self.conn

	def __exit__(self, exc_type, exc_value, exc_traceback):
		self.conn.close()

with DatabaseConnection() as conn:
		cursor = conn.cursor()
		cursor.execute("SELECT * FROM users")
		for row in cursor:
			print(row)
