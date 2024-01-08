""" import random
from operator import add, sub, mul



class user():
    def __init__(self, name, gender, element, weapon, tutorial):
        self.name = name
        self.gender = gender
        self.element = element
        self.weapon = weapon
        self.tutorial = tutorial

    def __str__(self):
        return f"{self.name}"
    def __str__(self):
        return f"{self.gender}"
    def __str__(self):
        return f"{self.element}"
    def __str__(self):
        return f"{self.weapon}"
    def __str__(self):
        return f"{self.tutorial}"

        


print("Welcome to Waifu Simulator!")
print()

#input a string
tutorial1 = input("Enter a name, gender, element, and weapon with a space separating each word: ")

#to separate the string by each word using spaces
split_tutorial1 = tutorial1.split()

#to find the first word of the string
first_word = split_tutorial1[0]
print("Hello,", first_word)


#level class in the game class and assign a set, lvl, hp, atk, speed, def, and quests for each level
class level(user):
    def __init__(self, lvl, hp, atk, speed, defense, quest):
        self.lvl = lvl
        self.hp = hp
        self.atk = atk
        self.speed = speed
        self.defense = defense
        self.quest = quest




lvl1 = level(1, 100, 5, 1, 0, ["Fight 3 slimes, Fight 3 hilichurls, Fight 1 bigchurls, Fight 2 abyss mages"])
lvl2 = level(2, 120, 10, 5, 10, ["Fight 10 slimes, Fight 10 hilichurls, Fight 2 bigchurls, Fight 2 abyss mages"])
lvl3 = level(3, 140, 20, 10, 20, ["Fight 15 slimes, Fight 15 Hilichurls, Fight 3 bigchurls, Fight 3 abyss mages, Fight 4 bandits"])
lvl4 = level(4, 160, 30, 20, 30, ["Fight 25 slimes, Fight 25 hilichurls, Fight 4 bigchurls, Fight 4 abyss mages, Fight 5 bandits, Fight 1 samurai"])
lvl5 = level(5, 180, 50, 30, 40, ["Fight 30 slimes, Fight 30 hilichurls, Fight 5 Bigchurls, Fight 5 Abyss Mages, Fight 8 bandits, Fight 2 samurai, fight 3 fatui agents"])
lvl6 = level(6, 200, 80, 40, 50, ["Fight 46 slimes, Fight 46 hilichurls, Fight 7 Bighchurls, Fight 8 abyss mages, Fight 11 bandits, fight 4 samurai, Fight 4 fatui agents, fight 3 robots"])
lvl7 = level(7, 220, 120, 50, 60, ["Fight 50 slimes, Fight 50 hilichurls, Fight 9 bigchurls, Fight 9 abyss mages, Fight 14 bandits, Fight 6 samurai, Fight 5 fatui agents, Fight 5 robots"])
lvl8 = level(8, 240, 170, 60, 70, ["Fight 72 slimes, Fight 75 hilichurls, Fight 10 bigchurls, FIght 15 abyss mages, Fight 16 bandits, Fight 8 samurai, Fight 7 fatui agents, Fight 6 robots, Fight 3 natureswayatgettingbackatus"])
lvl9 = level(9, 260, 230, 70, 80, ["Fight 80 slimes, Fight 80 hilichurls, Fight 15 bigchurls, Fight 20 abyss mages, Fight 10 samurai, Fight 10 fatui agents, Fight 10 robots, Fight 5 natureswayatgettingbackatus, Fight 1 bob"])
lvl10 = level(10, 300, 300, 80, 90, ["Fight 100 slimes, Fight 100 hilichurls, Fight 20 Bigchurls, Fight 30 abyss mages, FIght 25 bandits, Fight 15 samurai, Fight 15 fatui agents, Fight 20 robots, Fight 6 natureswayatgettingbackatus, Fight 10 bobs"])
print(lvl1.hp)

currentlvl = lvl1
remove_health = currentlvl.atk

print("\nYou are level 1 because you repel women lmao.")

#user input to see stats
tutorial2 = input("Would you like to see your stats for level 1? (Y/N): ").upper()

#if "Y" then print lvl1 stats, if "N" then L bozo
if tutorial2 == "Y":
    print("LVL:",lvl1.lvl, "HP:",lvl1.hp, "ATK:",lvl1.atk, "SPEED:",lvl1.speed, "DEF:",lvl1.defense)
else:
    print("...")


#user input to see quests
tutorial3 = input("Would you like to see your currently available quests? (Y/N): ").upper()

#if "Y" then print lvl1 quests, if "N" then you coward
if tutorial3 == "Y":
    print("QUESTS:",lvl1.quest)
else:
    print("Bruh you coward.")
print()


#enemy class in the game class to set, name, hp, atk, speed, def, of each enemy
class enemies(user):
    def __init__(self, name, hp, atk, speed, defense, grass):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.speed = speed
        self.defense = defense
        self.grass = grass
    def attack(self, enemies):
        enemies.hp = enemies.hp - currentlvl.atk

slimes = enemies("slimes", 5, 1, 1, 0, 2)
hilichurls = enemies("hilichurls", 5, 2, 2, 1, 3)
bigchurls = enemies("bigchurls", 10, 5, 5, 5, 7)
abyss_mages = enemies("abyss_mages", 15, 5, 5, 8, 13)
bandits = enemies("bandits", 80, 20, 20, 15, 15)
samurais = enemies("samurais", 100, 50, 50, 25, 20)
fatui_agents = enemies("fatui_agents", 125, 70, 70, 50, 50)
robots = enemies("robots", 170, 100, 100, 80, 75)
natureswayofgettingbackatus = enemies("natureswayofgettingbackatus", 200, 150, 150, 120, 100)
bob = enemies("bob", 1000, 500, 250, 150, 1000)


def Battle_info(enemies):
    print(f"{enemies.name} hp: {enemies.hp}, atk: {enemies.atk}, speed: {enemies.speed}, defense: {enemies.defense}, grass: {enemies.grass}")
    print(f"{first_word} hp: {currentlvl.hp}, atk: {currentlvl.atk}, speed: {currentlvl.speed}, defense: {currentlvl.defense}")
    print("your move first")
    ops = (add, sub, mul)
    op = random.choice(ops)
    mathnumber1, mathnumber2 = random.randint(1,12), random.randint(1,12)
    print(mathnumber1, op, mathnumber2)
    randommathproblem = int(op(mathnumber1, mathnumber2))
    mathproblem = input("answer:")
    if mathproblem == True:
        enemies.attack(enemies)
        print("hp:", {enemies.hp})
    else:
        print(":(")

checker = 0
tutorial4 = input("Would you like to start your quests? YOU CAN ONLY DO OTHER THINGS ONCE YOU COMPLETE THIS WARNINGGGG! NO GAME FOR YOU IF YOU SAY NO (Y/N): ").upper()
if tutorial4 == "Y":
    checker += 1
else:
    print("I guess you don't want to touch grass...")
    checker += 0
    
if checker == 1:
    print("You are walking towards the battle arena...")
    user1 = input("You have encountered a wild slime! Would you like to initiate a battle? (Y/N): ").upper()
if user1 == "Y":
    enemies = slimes
    Battle_info(enemies)

    
 """


from merchants import Merchant
#creates new instance of Merchant

Robert = Merchant("Robert", ["White Bread", "Croissant", "Garlic Bread", "Baguette"], ["8 grass", "8 grass", "8 grass", "8 grass"])
Jamie = Merchant("Jamie", ["Napoletana Pizza", "Risotto", "Gelato", "Lasagna", "Carbonara", "Spaghetti", "Fettuccine"], ["10 grass", "10 grass","10 grass", "10 grass", "10 grass", "10 grass", "10 grass"])






    





