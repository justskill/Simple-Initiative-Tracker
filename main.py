import tkinter as tk
from tkinter import simpledialog

class InitiativeTrackerGUI:
    def __init__(self, root):
        self.tracker = InitiativeTracker()
        self.root = root
        self.root.title("D&D Initiative Tracker")

        # Frame for inputs and buttons
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(padx=10, pady=5)

        # Name input
        self.name_label = tk.Label(self.input_frame, text="Name:")
        self.name_label.pack(side=tk.LEFT)
        self.name_entry = tk.Entry(self.input_frame)
        self.name_entry.pack(side=tk.LEFT, padx=5)

        # Initiative input
        self.initiative_label = tk.Label(self.input_frame, text="Initiative Roll:")
        self.initiative_label.pack(side=tk.LEFT)
        self.initiative_entry = tk.Entry(self.input_frame)
        self.initiative_entry.pack(side=tk.LEFT, padx=5)

        # Add button
        self.add_button = tk.Button(self.input_frame, text="Add Character", command=self.add_character)
        self.add_button.pack(side=tk.LEFT, padx=5)

        # Frame for list and next turn button
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        # Display area for initiative order
        self.listbox = tk.Listbox(self.frame, width=50, height=10)
        self.listbox.pack(side=tk.TOP, padx=5, pady=5)

        # Next Turn and Remove Character buttons
        self.next_turn_button = tk.Button(self.frame, text="Next Turn", command=self.next_turn)
        self.next_turn_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.remove_button = tk.Button(self.frame, text="Remove Character", command=self.remove_character)
        self.remove_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.update_list()

    def add_character(self):
        name = self.name_entry.get()
        initiative_roll_str = self.initiative_entry.get()
        if name and initiative_roll_str.isdigit():
            initiative_roll = int(initiative_roll_str)
            self.tracker.add_character(name, initiative_roll)
            self.update_list()
            # Clear the entry fields after adding
            self.name_entry.delete(0, tk.END)
            self.initiative_entry.delete(0, tk.END)
        else:
            tk.messagebox.showerror("Input Error", "Please enter a valid name and initiative roll.")

    def remove_character(self):
        try:
            # Get the selected character's name to remove
            selection = self.listbox.curselection()
            name = self.listbox.get(selection[0]).split(' ')[0]  # Assumes name is the first word
            self.tracker.remove_character(name)
            self.update_list()
        except IndexError:
            messagebox.showerror("Error", "No character selected")

    def next_turn(self):
        self.tracker.next_turn()
        self.update_list()

    def update_list(self):
        self.listbox.delete(0, tk.END)
        current_turn_index = self.tracker.current_turn_index
        for i, character in enumerate(self.tracker.list_characters()):
            display_text = character
            if i == current_turn_index:
                display_text = "> " + display_text
            self.listbox.insert(tk.END, display_text)

class InitiativeTracker:
    def __init__(self):
        self.characters = []
        self.current_turn_index = -1

    def current_turn_index(self):
        return self._current_turn_index

    def current_turn_index(self, value):
        self._current_turn_index = value

    def add_character(self, name, initiative_roll):
        self.characters.append({'name': name, 'initiative_roll': initiative_roll})
        self.characters.sort(key=lambda x: x['initiative_roll'], reverse=True)

    def next_turn(self):
        if self.characters:
            self.current_turn_index = (self.current_turn_index + 1) % len(self.characters)
            return self.characters[self.current_turn_index]['name']
        else:
            return "No characters in initiative."

    def find_character_index(self, name):
        for i, char in enumerate(self.characters):
            if char['name'] == name:
                return i
        return None

    def list_characters(self):
        return [f"{char['name']} with initiative {char['initiative_roll']}" for char in self.characters]

    def remove_character(self, name):
        self.characters = [char for char in self.characters if char['name'] != name]
        # Adjust current_turn_index if necessary
        if self.current_turn_index >= len(self.characters):
            self.current_turn_index = 0

    def write_initiative_list_to_file(self, filename="initiative_list.txt"):
        with open(filename, "w") as file:
            for char in self.characters:
                file.write(f"{char['name']} | {char['initiative_roll']}\n")

    def write_current_and_next_turn_to_file(self, filename="current_next_turn.txt"):
        if self.characters:
            current = self.characters[self.current_turn_index]['name']
            next_index = (self.current_turn_index + 1) % len(self.characters)
            next_turn = self.characters[next_index]['name']
            with open(filename, "w") as file:
                file.write(f"Current turn: {current}\nNext turn: {next_turn}\n")
        else:
            with open(filename, "w") as file:
                file.write("No characters in initiative.\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = InitiativeTrackerGUI(root)
    root.mainloop()
