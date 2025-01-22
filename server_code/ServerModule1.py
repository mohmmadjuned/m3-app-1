import anvil.server
from datetime import datetime

# Dictionary to store the diaries and their entries
diaries = {}

@anvil.server.call
def create_diary(diary_name):
    # Create a new diary
    if diary_name in diaries:
        return f"Diary '{diary_name}' already exists."
    diaries[diary_name] = []
    return f"Diary '{diary_name}' created!"

@anvil.server.call
def add_entry(diary_name, title, content):
    # Add a new entry to the specified diary
    if diary_name in diaries:
        entry = {
            "title": title,
            "content": content,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        diaries[diary_name].append(entry)
        return f"Entry '{title}' added successfully!"
    else:
        return f"Diary '{diary_name}' not found."

@anvil.server.call
def get_entries(diary_name):
    # Retrieve entries from a specific diary
    if diary_name in diaries:
        return diaries[diary_name]
    else:
        return []

@anvil.server.call
def delete_entry(diary_name, index):
    # Delete an entry by index
    if diary_name in diaries and 0 <= index < len(diaries[diary_name]):
        diaries[diary_name].pop(index)
        return f"Entry {index + 1} deleted successfully!"
    return "Invalid diary or entry index."
