import os
import time

# Folder to search
folder = "/Users/simonraw/PIYUSH/Python"

# Check each file in the folder
for filename in os.listdir(folder):
    if filename.endswith(".txt"):
        filepath = os.path.join(folder, filename)

        # Get last modified time
        modified_time = os.path.getmtime(filepath)

        # Convert to a readable date and time
        readable_time = time.ctime(modified_time)

        print("File Name:", filename)
        print("Last Modified:", readable_time)
        print("-" * 40)
