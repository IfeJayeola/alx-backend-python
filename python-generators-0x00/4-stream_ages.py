import seed

def stream_user_ages():
    connection = seed.connect_to_prodev()
    cursor = connection.cursor()

    cursor.execute("SELECT age FROM user_data")

    for (age,) in cursor:  # age comes back as a 1-tuple
        yield float(age)   # cast to float (optional if you're doing division)

    cursor.close()
    connection.close()

def compute_average_age():
    total = 0
    count = 0
    for age in stream_user_ages():
        total += age
        count += 1
    if count > 0:
        print(f"Average age of users: {total / count:.2f}")
    else:
        print("No users found.")
