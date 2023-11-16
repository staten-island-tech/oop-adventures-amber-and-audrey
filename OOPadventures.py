import json 
import os
with open("data.json", "r") as f:
    data = json.load(f)


class game():
    def __init__(self, name, gender, element, weapon):
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

class level(game):
    def __init__(self, lvl, hp, atk, speed, defense, quest):
        self.lvl = lvl
        self.hp = hp
        self.atk = atk
        self.speed = speed
        self.defense = defense
        self.quest = quest


class enemies(game):
    def __init__(self, slime, hilichurl, bigchurl, abyss_mage, samurai, bandit, fatui_agent, robot, natureswayofgettingbackatus, bob):
        self.slime = slime
        self.hilichurl = hilichurl
        self.bigchurl = bigchurl
        self.abyss_mage = abyss_mage
        self.samurai = samurai
        self.bandit = bandit
        self.fatui_agent = fatui_agent
        self.robot = robot
        self.natureswayofgettingbackatus = natureswayofgettingbackatus
        self.bob = bob

new_file = "updated.json"
with open(new_file, "w") as f:
    json_string = json.dumps(data)
    f.write(json_string)

os.remove("data.json")
os.rename(new_file, "data.json")