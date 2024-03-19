import mysql.connector

def retrieve_data_from_database(id_value):
    # Connect to the MySQL database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="$Tiger@0710$",
        database="project_app",
        port='3306'
    )
    cursor = conn.cursor()

    # Retrieve values from the SQL table based on the provided id_value
    cursor.execute('''SELECT * FROM WarriorData WHERE id = %s''', (id_value,))
    row = cursor.fetchone()

    # Assign retrieved values to variables
    WARRIOR_ANIMATION_STEPS = row[1]
    WARRIOR_SIZE = row[2]
    WARRIOR_SCALE = row[3]
    WARRIOR_OFFSET = [row[4], row[5]]
    IMAGE_LINK = row[6]

    # Close the database connection
    conn.close()

    return WARRIOR_ANIMATION_STEPS, WARRIOR_SIZE, WARRIOR_SCALE, WARRIOR_OFFSET, IMAGE_LINK