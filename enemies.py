import json 
import os
with open("enemies.json", "r") as f:
    # Serialize the updated Python list to a JSON string
    data = json.load(f)


class enemies():
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