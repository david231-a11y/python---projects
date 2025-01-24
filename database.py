import sqlite3

# Connect to the database (or create it if it doesn't exist)
connection = sqlite3.connect("nigeria.db")

# Create a cursor object to execute SQL commands
cursor = connection.cursor()

# Create the database and table
cursor.execute('''
CREATE TABLE IF NOT EXISTS state (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    state_name TEXT NOT NULL,
    city_capital TEXT NOT NULL,
    year INTEGER NOT NULL,
    age INTEGER NOT NULL
);
''')

# Insert sample data into the table
sample_data = [
    ("Lagos", "Ikeja", 1967, 56),
    ("Kano", "Kano", 1967, 56),
    ("Rivers", "Port Harcourt", 1967, 56),
    ("Oyo", "Ibadan", 1976, 47),
    ("Enugu", "Enugu", 1991, 32)
]

cursor.executemany('''
INSERT INTO state (state_name, city_capital, year, age)
VALUES (?, ?, ?, ?)
''', sample_data)

# Commit the changes
connection.commit()

# Fetch and display the contents of the table
print("Displaying the contents of the 'state' table:")
cursor.execute("SELECT * FROM state")
rows = cursor.fetchall()

# Print each row
for row in rows:
    print(row)

# Close the connection
connection.close()
