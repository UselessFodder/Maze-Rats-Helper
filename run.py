import json
import os

# Ensure the 'tables' directory exists
os.makedirs('tables', exist_ok=True)

# Table data for Tool Items, Treasure Items, Treasure Traits, and Valuable Materials
tables = {
    "tool_items": {
        "Name": "Tool Items",
        "Category": "Item",
        "1": ["Acid flask", "Bear trap", "Bellows", "Bolt-cutters", "Chain", "Chisel"],
        "2": ["Crowbar", "Door ram", "Ear trumpet", "Fire oil", "Fishing hook", "Goggles"],
        "3": ["Grappling hook", "Grease", "Hacksaw", "Hammer", "Hand drill", "Lantern"],
        "4": ["Lens", "Lock/key", "Lockpicks", "Manacles", "Metal file", "Mortar/pestle"],
        "5": ["Needle", "Pickaxe", "Pitchfork", "Pliers", "Pole", "Pulleys"],
        "6": ["Rope", "Scissors", "Shovel", "Spikes", "Steel wire", "Tongs"]
    },
    "treasure_items": {
        "Name": "Treasure Items",
        "Category": "Item",
        "1": ["Alchemy recipe", "Amulet", "Astrolabe", "Blueprints", "Calligraphy", "Carpet"],
        "2": ["Compass", "Contract", "Crown", "Crystal", "Deed", "Embroidery"],
        "3": ["Fine china", "Fine liquor", "Instrument", "Magical book", "Microscope", "Music box"],
        "4": ["Orrery", "Painting", "Perfume", "Prayer book", "Printing block", "Rare textile"],
        "5": ["Royal robes", "Saint's relic", "Scrimshaw", "Sextant", "Sheet music", "Signet ring"],
        "6": ["Silverware", "Spices", "Spyglass", "Tapestry", "Telescope", "Treasure map"]
    },
    "treasure_traits": {
        "Name": "Treasure Traits",
        "Category": "Item",
        "1": ["Altered", "Ancient", "Blessed", "Bulky", "Compact", "Consumable"],
        "2": ["Cultural value", "Cursed", "Damaged", "Disguised", "Draws enemies", "Effect"],
        "3": ["Element", "Embellished", "Encoded", "Exotic", "Extra-planar", "Famous"],
        "4": ["Forbidden", "Fragile", "Heavy", "Immovable", "Impractical", "Indestructible"],
        "5": ["Intelligent", "Masterwork", "Military value", "Non-human", "Owned", "Partial"],
        "6": ["Political value", "Religious value", "Repaired", "Royal", "Toxic", "Vile"]
    },
    "valuable_materials": {
        "Name": "Valuable Materials",
        "Category": "Item",
        "1": ["Alabaster", "Amber", "Aquamarine", "Azurite", "Beryl", "Black Pearl"],
        "2": ["Bloodstone", "Bone China", "Chalcedony", "Cinnabar", "Coral", "Diamond"],
        "3": ["Ebony", "Emerald", "Fire Agate", "Garnet", "Gold", "Ivory"],
        "4": ["Jade", "Jasper", "Jet", "Lapis Lazuli", "Malachite", "Moonstone"],
        "5": ["Onyx", "Opal", "Pearl", "Platinum", "Porcelain", "Ruby"],
        "6": ["Sapphire", "Serpentine", "Silver", "Star Iron", "Topaz", "Turquoise"]
    }
}

# Save each table as a separate JSON file
for table_name, table_data in tables.items():
    with open(f'tables/{table_name}.json', 'w') as file:
        json.dump(table_data, file, indent=4)
