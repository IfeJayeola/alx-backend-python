import uuid  # add this at the top if not already present

def insert_data(connection, filename):
    cursor = connection.cursor()
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            user_id = str(uuid.uuid4())  # generate a unique UUID
            name = row['name']
            email = row['email']
            age = row['age']

            cursor.execute("""
                INSERT IGNORE INTO user_data (user_id, name, email, age)
                VALUES (%s, %s, %s, %s)
            """, (user_id, name, email, age))

    connection.commit()
    cursor.close()
