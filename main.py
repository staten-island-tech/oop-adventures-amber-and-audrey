import random
from operator import add, sub, mul



class user():
    def __init__(self, name, gender, element, weapon, tutorial, inventory):
        self.name = name
        self.gender = gender
        self.element = element
        self.weapon = weapon
        self.tutorial = tutorial
        self.grass = grass
        self.inventory = inventory
    def buy(item):
        user.inventory.append(item)
        user.inventory.remove.grass(item)



print("Welcome to Waifu Simulator!")
print()

#input a string
tutorial1 = input("Enter a name, gender, element, and weapon with a space separating each word: ")
grass = 0
user.grass = grass
user.inventory = [user.grass]
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




lvl1 = level(1, 100, 5, 1, 0, ["Fight 1 slimes, Fight 1 hilichurls, Fight 1 bigchurls, Fight 1 abyss mages"])
lvl2 = level(2, 120, 10, 5, 10, ["Fight 2 slimes, Fight 2 hilichurls, Fight 2 bigchurls, Fight 2 abyss mages"])
lvl3 = level(3, 140, 20, 10, 20, ["Fight 3 slimes, Fight 3 Hilichurls, Fight 3 bigchurls, Fight 3 abyss mages, Fight 3 bandits"])
lvl4 = level(4, 160, 30, 20, 30, ["Fight 4 slimes, Fight 4 hilichurls, Fight 4 bigchurls, Fight 4 abyss mages, Fight 4 bandits, Fight 4 samurai"])
lvl5 = level(5, 180, 50, 30, 40, ["Fight 5 slimes, Fight 5 hilichurls, Fight 5 Bigchurls, Fight 5 Abyss Mages, Fight 5 bandits, Fight 5 samurai, fight 5 fatui agents"])
lvl6 = level(6, 200, 80, 40, 50, ["Fight 6 slimes, Fight 6 hilichurls, Fight 6 Bighchurls, Fight 6 abyss mages, Fight 6 bandits, fight 6 samurai, Fight 6 fatui agents, fight 6 robots"])
lvl7 = level(7, 220, 120, 50, 60, ["Fight 7 slimes, Fight 7 hilichurls, Fight 7 bigchurls, Fight 7 abyss mages, Fight 7 bandits, Fight 7 samurai, Fight 7 fatui agents, Fight 7 robots"])
lvl8 = level(8, 240, 170, 60, 70, ["Fight 8 slimes, Fight 8 hilichurls, Fight 8 bigchurls, FIght 8 abyss mages, Fight 8 bandits, Fight 8 samurai, Fight 8 fatui agents, Fight 8 robots, Fight 8 natureswayatgettingbackatus"])
lvl9 = level(9, 260, 230, 70, 80, ["Fight 9 slimes, Fight 9 hilichurls, Fight 9 bigchurls, Fight 9 abyss mages, Fight 9 samurai, Fight 9 fatui agents, Fight 9 robots, Fight 9 natureswayatgettingbackatus"])
lvl10 = level(10, 300, 300, 80, 90, ["Fight 10 slimes, Fight 10 hilichurls, Fight 10 Bigchurls, Fight 10 abyss mages, Fight 10 bandits, Fight 10 samurai, Fight 10 fatui agents, Fight 10 robots, Fight 10 natureswayatgettingbackatus, Fight 1 bobs"])
print(lvl1.hp)

currentlvl = lvl1


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
    def enemyattack(self, enemies):
        currentlvl.hp = currentlvl.hp - enemies.atk

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

class Battle():
    def Battle_info(enemy):
        print(f"{enemy.name} hp: {enemy.hp}, atk: {enemy.atk}, speed: {enemy.speed}, defense: {enemy.defense}, grass: {enemy.grass}")
        print(f"{first_word} hp: {currentlvl.hp}, atk: {currentlvl.atk}, speed: {currentlvl.speed}, defense: {currentlvl.defense}")
        while enemy.hp > 0:
            print("your move")
            ops = ("add", "sub", "mul")
            op = random.choice(ops)
            mathnumber1, mathnumber2 = random.randint(1,12), random.randint(1,12)
            if op == "add":
                print(mathnumber1, "+" ,mathnumber2)
                randommathproblem = mathnumber1 + mathnumber2
            elif op == "sub":
                print(mathnumber1,"-",mathnumber2)
                randommathproblem = mathnumber1 - mathnumber2
            elif op == "mul":
                print(mathnumber1,"x",mathnumber2)
                randommathproblem = mathnumber1 * mathnumber2
            else:
                print("bongo cat")
            mathanswer = int(input("answer:"))
            print(randommathproblem)
            if mathanswer == randommathproblem:
                enemy.attack(enemy)
                print(f"enemy hp: {enemy.hp}")
            else:
                print("enemies move it move it")
                enemy.enemyattack(enemy)
                print(f"your hp:{currentlvl.hp}")
        if currentlvl.hp == 0:
            print("your dead")
            battlemessage = input("battle again? (Y/N): ").upper()
            if battlemessage == "Y":
                enemy.hp = enemy.hp
                enemy.atk = enemy.atk
                currentlvl.hp = currentlvl.hp
                currentlvl.atk = currentlvl.atk
            if battlemessage == "N":
                return
        if enemy.hp == 0:
            print(f"{first_word}"+ " has won!")
            enemy.hp = enemy.hp
            enemy.atk = enemy.atk
            currentlvl.hp = currentlvl.hp
            currentlvl.atk = currentlvl.atk
 





            
        
    
checker = 0
tutorial4 = input("Would you like to start your quests? YOU CAN ONLY DO OTHER THINGS ONCE YOU COMPLETE THIS WARNINGGGG! NO GAME FOR YOU IF YOU SAY NO (Y/N): ").upper()
if tutorial4 == "Y":
    checker += 1
else:
    print("I guess you don't want to touch grass...")
    checker += 0
    
if checker == 1:
    print("You are walking towards the battle arena...")
    memem = input("You have encountered a wild slime! you have no choice (Y/N): ")
    Battle.Battle_info(slimes)
    user.grass += enemies.grass
    print("grass obtained: ")
    print(user.grass)
    print1 = input("This is grass, I know you dont know what it is but you get to touch it for the first time.")
    print2 = input("feels good?")
    print3 = input("bet it doesnt. You havent come out of your moms basement for 31 years.")
    print4 = input("What is wrong with you. 😲")
    print5 = input("Now you fight again UwU")
    Battle.Battle_info(slimes)
    user.grass += slimes.grass
    print("grass obtained: ")
    print(user.grass)
    Battle.Battle_info(slimes)
    user.grass += slimes.grass
    print("grass obtained: ")
    print(user.grass)
    Battle.Battle_info(hilichurls)
    user.grass += hilichurls.grass
    print("grass obtained: ")
    print(user.grass)
    Battle.Battle_info(hilichurls)
    user.grass += hilichurls.grass
    print("grass obtained: ")
    print(user.grass)
    Battle.Battle_info(hilichurls)
    user.grass += hilichurls.grass
    print("grass obtained: ")
    print(user.grass)
    Battle.Battle_info(bigchurls)
    user.grass += bigchurls.grass
    print("grass obtained: ")
    print(user.grass)
    Battle.Battle_info(abyss_mages)
    user.grass += abyss_mages.grass
    print("grass obtained: ")
    print(user.grass)
    



       