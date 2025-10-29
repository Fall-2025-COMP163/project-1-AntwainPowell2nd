"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [Antwain Powell]
Date: [Date]

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""
"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [Antwain Powell]
Date: [Date]

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""
import os # AI helped me use this as like an all seeing eye to check if a file exists after saving it.

def create_character(name, character_class):
    warrior_starter = {
        "name" : name,
        "class" : "Warrior",
        "level" : 1, 
        "strength" : 60, 
        "magic" : 10,
        "health" : 110,
        "gold" : 60
    }
    mage_starter = {
        "name" : name,
       "class" : "Mage",
       "level" : 1,
       "strength" : 15, 
       "magic" : 110, 
       "health" : 50,
       "gold" : 60 
    }
    rouge_starter = {
        "name" : name,
        "class" : "Rogue",
        "level" : 1,
        "strength" : 40,
        "magic" : 15,
        "health" : 75,
        "gold" : 60 
    }
    cleric_starter = {
        "name" : name,
        "class" : "Cleric",
        "level" : 1,
        "strength" : 20,
        "magic" : 90,
        "health" : 60,
        "gold" : 60 
    }
    if character_class == "Warrior":
        return warrior_starter
    elif character_class == "Mage":
        return mage_starter
    elif character_class == "Rogue":
        return rouge_starter 
    elif character_class == "Cleric":
        return cleric_starter

def calculate_stats(character_class, level):
    warrior_stats = level * 25, level * 5, level * 30
    mage_stats = level * 5, level * 35, level * 10
    rogue_stats = level * 15, level * 10, level * 20
    cleric_stats = level * 10, level * 30, level * 25
    if character_class == "Warrior":
        return warrior_stats
    elif character_class == "Mage":
        return mage_stats
    elif character_class == "Rouge":
        return rogue_stats 
    elif character_class == "Cleric":
        return cleric_stats 

def save_character(character, filename):
    with open(filename, 'w') as file:
        for key, value in character.items():
            if key.lower() == "name":
                file.write(f"Character Name: {value}\n")
                continue
            if key.lower() == "class":
                file.write(f"Class: {value}\n")
                continue
            else: 
                file.write(f"{key.capitalize()}: {value}\n")
            filename = character 
    return True

def load_character(filename):
    if os.path.exists(filename) == True:
        with open((f"{filename}"), 'r') as file:
            data = file.readlines()
            character = {}
            for i in data: 
                temp = i.split(":")
                key = temp[0].strip()
                value = temp[1].strip()
                if key == "Character Name":
                    key = "name"
                else:
                    key = key.lower()
                if value.isdigit():
                    value = int(value)
                character[key] = value  
            return character 


def display_character(character):
     with open(character, 'r') as file:
        data = file.readlines()
        for line in data:
            if ":" in line:
                key, value = line.split(":", 1)
                print(f"{key.strip()}: {value.strip()}") 

def level_up(character):
    with open(character, 'r') as file:
         data = file.readlines()
    updated_data = []
    character_class = None
    level = None
    for line in data:
        if "level" in line:
            key, value = line.split(":", 1)
            new_level = int(value.strip()) + 1
            updated_data.append(f"{key.strip()}: {new_level}\n")
            level = new_level
        elif "class" in line:
            key, value = line.split(":", 1)
            character_class = value.strip()
            updated_data.append(line)
        elif "Upgraded Stats" in line:
            updated_data.append(line)
    if character_class and level:
        stats = calculate_stats(character_class, level)
        updated_data.append(f"Upgraded Stats: {stats}\n") 
    with open(character, 'w') as file:
        file.writelines(updated_data)

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    
    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    save_character("Aj", "my_character.txt")
    loaded = load_character("my_character.txt") 

