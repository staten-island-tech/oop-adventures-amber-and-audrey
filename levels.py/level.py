import json
import os
with open("level.json", "r") as f:
    level = json.load(f)

questList= []
class level():
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
    questList.append(quest)
    base = {
        "lvl": lvl,
        "hp": hp,
        "atk": atk,
        "speed": speed,
        "defense": defense,
        "quest": questList
    }
    level.append(lvl, hp, atk, speed, defense, questList)
level()