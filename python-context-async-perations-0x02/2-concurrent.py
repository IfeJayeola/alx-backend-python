import asyncio
import aiosqlite

async def async_fetch_users():
	db = await aiosqlite.connect('users.db') 
	cursor = await db.execute("SELECT * FROM users")
	rows = await cursor.fetchall()
	for row in rows:
		print(row)
	await cursor.close()
	await db.close()
	return rows

async def async_fetch_older_users():
	db = await aiosqlite.connect('users.db')
	cursor = await db.execute("SELECT * FROM users WHERE age > ?", (25,))
	rows = await cursor.fetchall()
	for row in rows:
		print(row)
	await cursor.close()
	await db.close()
	return rows

async def fetch_concurrently():
	print('Initiating')
	result = await asyncio.gather( async_fetch_older_users(),  async_fetch_users())
	print('done')
	print(result)
	
asyncio.run(fetch_concurrently())

