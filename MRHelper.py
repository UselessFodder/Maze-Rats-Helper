#	Maze Rats Helper by UselessFodder
# This program is designed to help GMs run the Maze Rats RPG system by
# Ben Milton. The initial design goal is to allow GMs to execute single or
# multiple generations of every type of table within the Maze Rats source book

# Full Disclosure: Some of this code was generated with the help of ChatGPT

# imports
import tkinter as tk
import random
import json
import os

# ***TODO: Move tables to external library
# Define the monster features table
#monster_features = {
#    1: ["Antlers", "Beak", "Carapace", "Claws", "Compound eyes", "Eye Stalks"],
#    2: ["Fangs", "Fins", "Fur", "Gills", "Hooves", "Horns"],
#    3: ["Legless", "Long tongue", "Many-eyed", "Many-limbed", "Mucus", "Pincers"],
#    4: ["Plates", "Plumage", "Proboscis", "Scales", "Segments", "Shaggy hair"],
#    5: ["Shell", "Spikes", "Spinnerets", "Spines", "Stinger", "Suction cups"],
#    6: ["Tail", "Talons", "Tentacles", "Trunk", "Tusks", "Wings"]
#}

def load_tables(directory):
    tables = {}
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            with open(os.path.join(directory, filename), 'r') as file:
                table_name = os.path.splitext(filename)[0]
                new_table = json.load(file)
                #tables[table_name] = json.load(file)
                tables[table_name] = new_table
                category = new_table.get("Category")
                if category not in table_types:
                    table_types.append(category)
    return tables

# all types of tables used to generate buttons
table_types = []

# load all tables within the tables directory
tables = load_tables('tables')

def roll_dice():
    return random.randint(1, 6), random.randint(1, 6)

def generate_feature():
    table_name = 'monster_features'
    group, item = roll_dice()
    feature = tables[table_name][str(group)][item - 1]
    #result_label.config(text=f"Group {group}, Item {item}: {feature}")
    result_label.config(text=f"Result: ({group}, {item}): {feature}")

# Setup the main application window
root = tk.Tk()
root.geometry("600x400")
root.title("Maze Rats Helper")

# create a frame to hold buttons
buttons = tk.Frame(root, padx=10)

# Create a button to generate a monster feature
generate_button = tk.Button(buttons, text="Generate Monster Feature", command=generate_feature)
generate_button.pack(pady=20)

# create buttons for all categories
for x in table_types:
    new_button = tk.Button(buttons, text=x)
    new_button.pack(pady=10)

# Label to display the result
result_label = tk.Label(root, text="", font=("Helvetica", 16))
result_label.config(text=f"Table Types: {table_types}")
result_label.pack(pady=20)

# Start the application
buttons.pack()
root.mainloop()
