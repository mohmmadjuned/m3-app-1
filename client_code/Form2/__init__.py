from ._anvil_designer import Form2Template
from anvil import *
import anvil.server

class Form2(Form2Template):
    def __init__(self, **properties):
        self.init_components(**properties)
        self.diary_name = ""  # Store the current diary name

    def create_diary_button_click(self, **event_args):
        """Called when the 'Create Diary' button is clicked."""
        self.diary_name = self.diary_name_textbox.text
        if self.diary_name:
            result = anvil.server.call('create_diary', self.diary_name)  # Use the function name as a string
            alert(result)
        else:
            alert("Please enter a diary name.")

    def add_entry_button_click(self, **event_args):
        """Called when the 'Add Entry' button is clicked."""
        title = self.entry_title_textbox.text
        content = self.entry_content_textarea.text
        if self.diary_name and title and content:
            result = anvil.server.call('add_entry', self.diary_name, title, content)  # Function name as a string
            alert(result)
            self.load_entries()  # Reload entries after adding
        else:
            alert("Please ensure all fields are filled.")

    def load_entries(self):
        """Load entries for the current diary."""
        if self.diary_name:
            entries = anvil.server.call('get_entries', self.diary_name)  # Function name as a string
            self.entries_repeating_panel.items = entries

    def delete_entry_button_click(self, index, **event_args):
        """Called when the 'Delete Entry' button is clicked."""
        if self.diary_name:
            result = anvil.server.call('delete_entry', self.diary_name, index)  # Function name as a string
            alert(result)
            self.load_entries()  # Reload entries after deletion
