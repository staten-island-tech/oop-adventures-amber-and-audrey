
import json 
import os

print("Hello, player. Welcome to waifu simulator.")
with open("game.json", "r") as f:
    jsonLoad = json.load(f)
name = 'o'
gender = 'o'
element = 'o'
weapon = "a"

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
    def base(base):
        base = {
            "name": name,
            "gender": gender,
            "element": element,
            "weapon": weapon
}
    jsonLoad.append(base)
    print("Hello", name)
    print 
    if base == []:
        print("You are level 1 because you repel women lmao.")
    
        with open("game.json", "r") as f:
            jsonLoad = json.load(f)

game.player(self, name, gender, element, weapon)
jsonLoad.append(game.base)

new_file = "updated.json"
with open(new_file, "w") as f:
    json_string = json.dumps(jsonLoad)
f.write(json_string)

os.remove("game.json")
os.rename(new_file, "game.json")

class level(game):
    def createLevel(self, lvl, hp, atk, speed, defense, quest):
        self.lvl = lvl
        self.hp = hp
        self.atk = atk
        self.speed = speed
        self.defense = defense
        self.quest = quest
    questList= []

    firstmessage = input("would you like to complete the quest provided to level up? (Y/N)")
    if firstmessage == ("Y"):
        print(lvl.quest)


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

enemies = enemies()
game = game()
level = level()


def battlesystem():
    

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

