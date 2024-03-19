# import mysql.connector
#
# # Connect to the MySQL database
# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="$Tiger@0710$",
#     database="project_app",
#     port='3306'
# )
#
# cursor = conn.cursor()
#
# # Retrieve values from the SQL table
# cursor.execute('''SELECT * FROM WarriorData WHERE id = %s''',(value))
# row = cursor.fetchone()
#
# # Assign retrieved values to variables
# # w_a_s = row[1]
# W_SI = row[2]
# W_SC = row[3]
# W_OFF = [row[4], row[5]]
# IMAGE_LINK = row[6]
#
#
# # Close the database connection
# conn.close()