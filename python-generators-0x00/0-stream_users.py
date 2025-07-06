import seed  # reuse our database connection setup

def stream_users():
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM user_data")

    for row in cursor:
        yield row  # yield each row one by one

    cursor.close()
    connection.close()
