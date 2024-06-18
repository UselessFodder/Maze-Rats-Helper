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

def load_complex(directory):
    complex_tables = {}
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            with open(os.path.join(directory, filename), 'r') as file:
                table_name = os.path.splitext(filename)[0]
                new_table = json.load(file)
                #tables[table_name] = json.load(file)
                complex_tables[table_name] = new_table
                #print(new_table.get("Tables")[1])
                category = new_table.get("Category")
                if category not in table_types:
                    table_types.append(category)
                    
    return complex_tables

def name_lookup(name):
    for x in tables:
        current_table = tables.get(x)
        if current_table.get("Name") == name:
            return x

def sub_menu(category):
    #open a new window with category name
    window = tk.Tk()
    #window.geometry("400x200")
    window.title(f"{category} Tables")
    sub_panel = tk.Frame(window, width=200, height=200)
    sub_panel.grid(row=0, column=0, padx=10)
    sub_panel.pack_propagate(0)
    sub_label = tk.Label(sub_panel, wraplength=180, text="")
    sub_label.pack()
    #sub_panel.pack(pady=20)
    sub_buttons = tk.Frame(window, padx=10)
    sub_buttons.grid(row=0, column=1)
    
    #create buttons for all tables in category
    for x in tables:
        current_table = tables.get(x)
        if current_table.get("Category") == category:
            new_button = tk.Button(sub_buttons, text=tables.get(x).get("Name"), command=partial(generate,x,sub_label))
            new_button.pack(pady=5)
            
    #create buttons for complex actions
    for x in complex_tables:
        current_table = complex_tables.get(x)
        if complex_tables.get(x).get("Category") == category:
            new_button = tk.Button(sub_buttons, text=complex_tables.get(x).get("Name"), font='Helvetica 10 bold', command=partial(generate_complex,current_table.get("Tables"),sub_label))
            new_button.pack(pady=5)
    
    #add clear button to erase label
    clear_button = tk.Button(sub_buttons, text='Clear', font='Helvetica 12 bold', command=partial(clear_label,sub_label))
    clear_button.pack(pady=10)
    
    window.mainloop()

def clear_label(label):
    label.config(text='')

def roll_dice():
    return random.randint(1, 6), random.randint(1, 6)

def generate(table_name, panel_name):
    #***debug
    #table_name = 'monster_features'
    
    result = roll_table(table_name)
    
    panel_name.config(text=panel_name["text"] + result)

def generate_complex(table_list, panel_name):
    clear_label(panel_name)
    result = ""
    for x in table_list:
        result = result + roll_table(name_lookup(x))
    
    panel_name.config(text=panel_name["text"] + result)

def roll_table(table_name):
    group, item = roll_dice()
    result = tables[table_name][str(group)][item - 1]
    
    #check if complex table result
    if str(result)[0] == "*":
        next_table = name_lookup(result[1:])
        if debug_mode == True:
            result = f"{tables[table_name].get('Name')[:-1]}: {result[1:]} ({group}, {item})\n" + roll_table(next_table)
        else:
            result = f"{tables[table_name].get('Name')[:-1]}: {result[1:]}\n" + roll_table(next_table)
    else:
        if debug_mode == True:
            result = f"{tables[table_name].get('Name')[:-1]}: {result} ({group}, {item})\n"
        else:
            result = f"{tables[table_name].get('Name')[:-1]}: {result}\n"
        
    total_result = result
    return total_result


#debug mode that shows more information
debug_mode = False

# all types of tables used to generate buttons
table_types = []

# load all tables within the tables directory
tables = load_tables('tables')

# load all complex actions within complex folder
complex_tables = load_complex('complex')

# Setup the main application window
root = tk.Tk()
#root.geometry("600x400")
root.title("Maze Rats Helper")

# create a frame to hold buttons
buttons = tk.Frame(root, padx=10)

# create buttons for all categories
for x in table_types:
    new_button = tk.Button(buttons, text=x, command=partial(sub_menu,x))
    new_button.pack(pady=5)

# Label prompt user
result_label = tk.Label(root, text="", font=("Helvetica", 16))
#result_label.config(text=f"Table Types: {table_types}")
result_label.config(text=f"   Maze Rats Helper   ")
result_label.pack(pady=10)

# Start the application
buttons.pack()
root.mainloop()
