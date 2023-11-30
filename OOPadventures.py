import json 
import os

with open("game.json", "r") as f:
    jsonLoad = json.load(f)
name = 'o'
gender = 'o'
element = 'o'
weapon = 'o'

lvl = 1
hp = 1
atk = 1
speed = 1
defense = 1
quest = 'o'

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
    jsonLoad.append(base)




class level(game):
    def createLevel(self, lvl, hp, atk, speed, defense, quest):
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
    jsonLoad.append(base)



class enemies(game):
    def enemyCreate(self, name, hp, atk, speed, defense):
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
    jsonLoad.append(base)    
enemies = enemies()
game = game()
level = level()



with open("game.json", "r") as f:
    jsonLoad = json.load(f)

    game.player(name, gender, element, weapon)
    jsonLoad.append(game.base)

new_file = "updated.json"
with open(new_file, "w") as f:
    json_string = json.dumps(jsonLoad)
    f.write(json_string)

os.remove("game.json")
os.rename(new_file, "game.json")



with open("level.json", "r") as f:
    jsonLoad = json.load(f)

    level.createLevel(lvl, hp, atk, speed, defense, quest)
    jsonLoad.append(level.base)

new_file = "updated.json"
with open(new_file, "w") as f:
    json_string = json.dumps(jsonLoad)
    f.write(json_string)

os.remove("level.json")
os.rename(new_file, "level.json")



with open("enemies.json", "r") as f:
    jsonLoad = json.load(f)

    enemies.enemyCreate(name, hp, atk, speed, defense)
    jsonLoad.append(enemies.base)

new_file = "updated.json"
with open(new_file, "w") as f:
    json_string = json.dumps(jsonLoad)
    f.write(json_string)

os.remove("enemies.json")
os.rename(new_file, "enemies.json")

