import json 
import os
with open("data.json", "r") as f:
    # Serialize the updated Python list to a JSON string
    data = json.load(f)

class game():
    def player(self, name, gender, element, weapon):
        self.name = name
        self.gender = gender
        self.element = element
        self.weapon = weapon
    def __str__(self):
        return f"{self.name}"
    def __str__(self):
        return f"{self.gender}"
    def __str__(self):
        return f"{self.element}"
    def __str__(self):
        return f"{self.weapon}"
    
    name = input("Enter your name: ")
    gender = input("Enter your gender: ")
    element = input("Enter your element: ")
    weapon = input("Enter your weapon: ")
    base = {
        "name": name,
        "gender": gender,
        "element": element,
        "weapon": weapon
}
    data.append(base)

new_file = "updated.json"
with open(new_file, "w") as f:
    json_string = json.dumps(data)
    f.write(json_string)

os.remove("game.json")
os.rename(new_file, "game.json")



import json 
import os
with open("data.json", "r") as f:
    # Serialize the updated Python list to a JSON string
    data = json.load(f)

class level(game):
    def __init__(self, lvl, hp, atk, speed, defense, quest):
        self.lvl = lvl
        self.hp = hp
        self.atk = atk
        self.speed = speed
        self.defense = defense
        self.quest = quest
    lvl = int(input("Enter a lvl: "))
    hp = int(input("Enter hp: "))
    atk = int(input("Enter atk: "))
    speed = int(input("Enter speed: "))
    defense = int(input("Enter defense: "))
    quest = input("Enter quest: ")
    questList= []
    questList.append(quest)
    base = {
        "lvl": lvl,
        "hp": hp,
        "atk": atk,
        "speed": speed,
        "defense": defense,
        "quest": questList
    }
    data.append(base)

new_file = "updated.json"
with open(new_file, "w") as f:
    json_string = json.dumps(data)
    f.write(json_string)
os.remove("level.json")
os.rename(new_file,"level.json")
  
import json 
import os
with open("enemies.json", "r") as f:
    # Serialize the updated Python list to a JSON string
    data = json.load(f)



class enemies(game):
    def __init__(self, name, hp, atk, speed, defense):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.speed = speed
        self.defense = defense
    name = input("Enter the enemies' name: ")
    hp = int(input("Enter hp: "))
    atk = int(input("Enter atk: "))
    speed = int(input("Enter speed: "))
    defense = int(input("Enter defense: "))
    base = {
    "name": name,
    "hp": hp,
    "atk": atk,
    "speed": speed,
    "defense": defense
}
    data.append(base)    

new_file = "updated.json"
with open(new_file, "w") as f:
    json_string = json.dumps(data)
    f.write(json_string)

os.remove("enemies.json")
os.rename(new_file, "enemies.json")
