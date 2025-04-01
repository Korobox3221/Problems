import sqlite3

# Connect to the database
conn = sqlite3.connect('visitors.db')
c = conn.cursor()
c.execute("SELECT * FROM visitors LIMIT 1")

# Get column names from cursor.description
columns = [description[0] for description in c.description]

print("Columns in 'visitors' table:")
for column in columns:
    print(column)
# Fetch and print all rows
c.execute("SELECT * FROM visitors")

rows = c.fetchall()
for row in rows:
    print(row)

# Close the connection
conn.close()