# D&D Initiative Tracker

This project is a graphical user interface (GUI) tool designed to assist Dungeon Masters (DMs) in managing initiative order during D&D (or other TTRPG) gameplay . It allows you to add characters, sort them by initiative rolls, track turns, and remove characters from the initiative list.  Please note that this software is designed to be used in conjunction with OBS to display the contents of the text file outputs.

## Features

- **Add Characters**: Add a character's name and their initiative roll to the tracker.
- **View Initiative Order**: Automatically sorts characters based on their initiative rolls in descending order.
- **Next Turn Management**: Highlight and progress through the current turn in the initiative order.
- **Remove Characters**: Remove characters from the initiative list as needed.
- **File Output**:
  - Save the full initiative list to a file (`initiative_list.txt`).
  - Save the current and next turn information to a file (`current_next_turn.txt`).

## Requirements

- Python 3.7 or later
- `tkinter` (usually included by default with Python installations)

## Installation

1. Clone or download this repository to your local machine.
2. Ensure you have Python 3 installed on your system.
3. Run the script using:

   ```bash
   python main.py
