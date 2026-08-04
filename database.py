# Import the sqlite3 module to work with SQLite databases
import sqlite3

# Create a tuple containing the supplied file names
fileList = (
    'information.docx',
    'Hello.txt',
    'myImage.png',
    'myMovie.mpg',
    'World.txt',
    'data.pdf',
    'myPhoto.jpg'
)

# Connect to (or create) the SQLite database
conn = sqlite3.connect("TextFiles.db")

# Create a cursor object
cur = conn.cursor()

# Create a table with:
# 1. An auto-incrementing integer primary key
# 2. A text field for the file name
cur.execute("""
CREATE TABLE IF NOT EXISTS tbl_files (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    FileName TEXT
)
""")

# Loop through the list of file names
for file in fileList:
    # Check if the file ends with .txt
    if file.endswith(".txt"):
        # Insert the file name into the database
        cur.execute("INSERT INTO tbl_files (FileName) VALUES (?)", (file,))

# Save the changes
conn.commit()

# Print the qualifying text files from the database
print("Text files stored in the database:\n")

for row in cur.execute("SELECT * FROM tbl_files"):
    print(f"ID: {row[0]} | File Name: {row[1]}")

# Close the database connection
conn.close()