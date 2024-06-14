import json
import os

# Ensure the 'tables' directory exists
os.makedirs('tables', exist_ok=True)

# Table data for Magic section from the Maze Rats rules

tables = {
    "physical_effects": {
        "Category": "Magic",
        "1": ["Animating", "Attracting", "Binding", "Blossoming", "Consuming", "Creeping"],
        "2": ["Crushing", "Diminishing", "Dividing", "Duplicating", "Enveloping", "Expanding"],
        "3": ["Fusing", "Grasping", "Hastening", "Hindering", "Illuminating", "Imprisoning"],
        "4": ["Levitating", "Opening", "Petrifying", "Phasing", "Piercing", "Pursuing"],
        "5": ["Reflecting", "Regenerating", "Rending", "Repelling", "Resurrecting", "Screaming"],
        "6": ["Sealing", "Shapeshifting", "Shielding", "Spawning", "Transmuting", "Transporting"]
    },
    "physical_forms": {
        "Category": "Magic",
        "1": ["Altar", "Armor", "Arrow", "Beast", "Blade", "Cauldron"],
        "2": ["Chain", "Chariot", "Claw", "Cloak", "Colossus", "Crown"],
        "3": ["Elemental", "Eye", "Fountain", "Gate", "Golem", "Hammer"],
        "4": ["Horn", "Key", "Mask", "Monolith", "Pit", "Prison"],
        "5": ["Sentinel", "Servant", "Shield", "Spear", "Steed", "Swarm"],
        "6": ["Tentacle", "Throne", "Torch", "Trap", "Wall", "Web"]
    },
    "ethereal_elements": {
        "Category": "Magic",
        "1": ["Ash", "Chaos", "Distortion", "Dream", "Dust", "Echo"],
        "2": ["Ectoplasm", "Fire", "Fog", "Ghost", "Harmony", "Heat"],
        "3": ["Light", "Lightning", "Memory", "Mind", "Mutation", "Negation"],
        "4": ["Plague", "Plasma", "Probability", "Rain", "Rot", "Shadow"],
        "5": ["Smoke", "Snow", "Soul", "Star", "Stasis", "Steam"],
        "6": ["Thunder", "Time", "Void", "Warp", "Whisper", "Wind"]
    },
    "ethereal_effects": {
        "Category": "Magic",
        "1": ["Avenging", "Banishing", "Bewildering", "Blinding", "Charming", "Communicating"],
        "2": ["Compelling", "Concealing", "Deafening", "Deceiving", "Deciphering", "Disguising"],
        "3": ["Dispelling", "Emboldening", "Encoding", "Energizing", "Enlightening", "Enraging"],
        "4": ["Excruciating", "Foreseeing", "Intoxicating", "Maddening", "Mesmerizing", "Mindreading"],
        "5": ["Nullifying", "Paralyzing", "Revealing", "Revolting", "Scrying", "Silencing"],
        "6": ["Soothing", "Summoning", "Terrifying", "Warding", "Wearying", "Withering"]
    },
    "physical_elements": {
        "Category": "Magic",
        "1": ["Acid", "Amber", "Bark", "Blood", "Bone", "Brine"],
        "2": ["Clay", "Crow", "Crystal", "Ember", "Flesh", "Fungus"],
        "3": ["Glass", "Honey", "Ice", "Insect", "Lava", "Metal"],
        "4": ["Moss", "Obsidian", "Oil", "Poison", "Rat", "Salt"],
        "5": ["Sand", "Sap", "Serpent", "Slime", "Stone", "Tar"],
        "6": ["Thorn", "Vine", "Water", "Wine", "Wood", "Worm"]
    },
    "ethereal_forms": {
        "Category": "Magic",
        "1": ["Aura", "Beacon", "Beam", "Blast", "Blob", "Bolt"],
        "2": ["Bubble", "Call", "Cascade", "Circle", "Cloud", "Coil"],
        "3": ["Cone", "Cube", "Dance", "Disk", "Field", "Form"],
        "4": ["Gaze", "Loop", "Moment", "Nexus", "Portal", "Pulse"],
        "5": ["Pyramid", "Ray", "Shard", "Sphere", "Spray", "Storm"],
        "6": ["Swarm", "Torrent", "Touch", "Vortex", "Wave", "Word"]
    }
}

# Save each table as a separate JSON file
for table_name, table_data in tables.items():
    with open(f'tables/{table_name}.json', 'w') as file:
        json.dump(table_data, file, indent=4)

