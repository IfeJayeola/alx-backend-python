import sqlite3 
import functools


def with_db_connection(func):
	def wrapper(*args, **kwargs):
		conn  = sqlite3.connect('users.db')
		try:
			return func(conn,*args, **kwargs)
		finally:
			conn.close()
	return wrapper

def transactional(func):
	def wrapper(*args, **kwargs):
		conn = args[0]
		try:
			result = func(*args, **kwargs)
			conn.commit()
			return result
		except Exception as e:
			conn.rollback()
			print(e)
			raise
	return wrapper
"""your code goes here"""

@with_db_connection 
@transactional 
def update_user_email(conn, user_id, new_email): 
	cursor = conn.cursor() 
	cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id)) 
#### Update user's email with automatic transaction handling 

update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')
