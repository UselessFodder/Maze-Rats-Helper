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
from functools import partial

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

def sub_menu(category):
    #open a new window with category name
    window = tk.Tk()
    #window.geometry("400x200")
    window.title(f"{category} Tables")
    sub_panel = tk.Frame(window, width=200, height=200)
    sub_panel.grid(row=0, column=0, padx=10)
    sub_panel.pack_propagate(0)
    sub_label = tk.Label(sub_panel, text="")
    sub_label.pack()
    #sub_panel.pack(pady=20)
    sub_buttons = tk.Frame(window, padx=10)
    sub_buttons.grid(row=0, column=1)
    
    #create buttons for all tables in category
    for x in tables:
        current_table = tables.get(x)
        if current_table.get("Category") == category:
            new_button = tk.Button(sub_buttons, text=x, command=partial(generate,x,sub_label))
            new_button.pack(pady=10)
            
    #add clear button to erase label
    clear_button = tk.Button(sub_buttons, text='Clear', font='Helvetica 12 bold', command=partial(clear_label,sub_label))
    clear_button.pack(pady=10)
    
    window.mainloop()

def clear_label(label):
    label.config(text='')

def roll_dice():
    return random.randint(1, 6), random.randint(1, 6)

def generate(table_name, panel_name):
    #table_name = 'monster_features'
    group, item = roll_dice()
    feature = tables[table_name][str(group)][item - 1]
    #result_label.config(text=f"Group {group}, Item {item}: {feature}")
    panel_name.config(text=panel_name["text"] + f"{tables[table_name].get('Name')}: {feature} ({group}, {item})\n")

# Setup the main application window
root = tk.Tk()
#root.geometry("600x400")
root.title("Maze Rats Helper")

# create a frame to hold buttons
buttons = tk.Frame(root, padx=10)

# Create a button to generate a monster feature
#generate_button = tk.Button(buttons, text="Generate Monster Feature", command=partial(generate,'monster_features'))
#generate_button.pack(pady=20)

# create buttons for all categories
for x in table_types:
    new_button = tk.Button(buttons, text=x, command=partial(sub_menu,x))
    new_button.pack(pady=10)

# Label to display the result
result_label = tk.Label(root, text="", font=("Helvetica", 16))
result_label.config(text=f"Table Types: {table_types}")
result_label.pack(pady=20)

# Start the application
buttons.pack()
root.mainloop()
