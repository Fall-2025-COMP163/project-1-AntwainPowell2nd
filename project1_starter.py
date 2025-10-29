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
        "class" : "Rouge",
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
    elif character_class == "Rouge":
        return rouge_starter 
    elif character_class == "Cleric":
        return cleric_starter

def calculate_stats(character_class, level):
    if level >= 1 and level < 5:
        warrior_stats = "medium strength", "very low magic", "medium health"
        mage_stats = "very low strength", "medium magic", "low health"
        rouge_stats = "low strength", "very low magic", "low-medium health"
        cleric_stats = "very low strength", "medium magic", "medium health"
    elif level >= 5 and level < 10:
        warrior_stats = "high strength", "low magic", "high health"
        mage_stats = "low strength", "high magic", "low-medium health"
        rouge_stats = "medium strength", "low magic", "medium-high health"
        cleric_stats = "low strength", "high magic", "high health"
    elif level >= 10 and level < 15:
        warrior_stats = "very high strength", "medium magic", "very high health"
        mage_stats = "medium strength", "very high magic", "medium health"
        rouge_stats = "high strength", "medium magic", "high health"
        cleric_stats = "medium strength", "very high magic", "very high health"
    elif level >= 15:
        warrior_stats = "extreme strength", "high magic", "extreme health"
        mage_stats = "high strength", "extreme magic", "high health"
        rouge_stats = "very high strength", "high magic", "very high health"
        cleric_stats = "high strength", "extreme magic", "extreme health"
    if character_class == "Warrior":
        return warrior_stats
    elif character_class == "Mage":
        return mage_stats
    elif character_class == "Rouge":
        return rouge_stats 
    elif character_class == "Cleric":
        return cleric_stats

def save_character(character, filename):
    success = False
    if character and filename:  
        with open(filename, 'w') as file:
            for key, value in character.items():
                file.write(f"{key}: {value}\n")
        success = os.path.exists(filename)# AI helped with file I/O error handling logic in save_character function
    return success 

def load_character(filename):
    with open(filename, 'r') as file:
        data = file.readlines()
        return data 

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
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")

