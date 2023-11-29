import json 
import os
with open("game.json", "r") as f:
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