import json
import os

# Ensure the 'tables' directory exists
os.makedirs('tables', exist_ok=True)

# Table data for Assets and NPC Goals
tables = {
    "assets": {
        "Name": "Assets",
        "Category": "Character",
        "1": ["Authority", "Avoids detection", "Calls in favors", "Charming", "Cooks the books", "Erases evidence"],
        "2": ["Excellent liar", "Extremely rich", "Faction-leader", "Faction-member", "Feared", "Fortified base"],
        "3": ["Gorgeous", "Hears rumors", "Huge family", "Huge library", "Impersonator", "Interrogator"],
        "4": ["Knows a guy", "Knows a way in", "Launders money", "Learned", "Local celebrity", "Local knowledge"],
        "5": ["Loyal henchmen", "Middling oracle", "Nothing to lose", "Owns the guards", "Powerful spouse", "Procures gear"],
        "6": ["Pulls the strings", "Secret lab", "Sells contraband", "Smuggles goods", "Spy network", "War hero"]
    },
    "npc_goals": {
        "Name": "NPC Goals",
        "Category": "Character",
        "1": ["A better life", "Acceptance", "Acquire item", "Craft item", "Destroy faction", "Destroy item"],
        "2": ["Enlightenment", "Fame", "Found faction", "Freedom", "Glory", "Impress NPC"],
        "3": ["Infamy", "Infiltrate faction", "Justice", "Kidnap NPC", "Lead faction", "Learning"],
        "4": ["Locate NPC", "Love", "Mastery", "Power", "Reach location", "Rescue NPC"],
        "5": ["Resolve dispute", "Restore faction", "Reveal a secret", "Revenge", "Sabotage faction", "Serve a deity"],
        "6": ["Serve evil", "Serve faction", "Serve ideology", "Serve leader", "Serve the needy", "Wealth"]
    }
}

# Save each table as a separate JSON file
for table_name, table_data in tables.items():
    with open(f'tables/{table_name}.json', 'w') as file:
        json.dump(table_data, file, indent=4)
