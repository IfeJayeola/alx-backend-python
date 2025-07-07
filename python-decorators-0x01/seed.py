import sqlite3

# Connect to (or create) the database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Create the users table with an email column
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    message TEXT NOT NULL,
    email TEXT
)
""")

# Optional: Clear any existing data
cursor.execute("DELETE FROM users")

# Insert sample users
users = [
    ("Ifeoluwa", "Welcome!", "ifeoluwa@example.com"),
    ("Ada", "Good morning", "ada@example.com"),
    ("Tunde", "Hi there", "tunde@example.com"),
]

cursor.executemany("INSERT INTO users (name, message, email) VALUES (?, ?, ?)", users)

# Save changes and close the connection
conn.commit()
conn.close()

print("Database seeded successfully.")
