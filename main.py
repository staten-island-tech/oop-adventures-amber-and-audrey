<<<<<<< HEAD
import random
from operator import add, sub, mul
from merchants import Merchants
=======
from classes import user, slime, hilichurl, bigchurl, abyss_mage, bandit, samurai, natureswayofgettingbackatus, bob

>>>>>>> 37347096dc02efa11206b6e52113887664513fad


#player
player = user("Traveler", 100)

#enemies
slim = slime("Slime", 10, 5)
hilichur = hilichurl("Hilichurl", 30, 5)
bigchur = bigchurl("Bigchurl", 50, 10)
abyss_mag = abyss_mage("Abyss Mage", 70, 10)
bandi = bandit("Bandit", 90, 15)
samura = samurai("Samurai", 110, 15)
natureswayofgettingbackatu = natureswayofgettingbackatus("Natureswayofgettingbackatu", 130, 20)
bo = bob("bob", 150, 25)

#start of game     
print("Welcome to Waifu Simulator!")
print()
name = input("What is your name? ")
print("Hello,", name)
tut1 = input("This journey is going to be a tough one, but you will be rewarded generously... With grass of course :)")
tut2 = input("You'll start off with a wooden sword, but with each level of enemy you defeat, you gain a better weapon")
tut3 = input("Anyways, enough talking and get into action!")
tut4 = input("You are now walking towards the battle arena...")
print()
#slime fight
tut5 = input("You have encountered a slime!!")
if player.hp > 0:
    from battle import slime_fight, hilichurl_fight, bigchurl_fight, abyssmage_fight, bandit_fight, samurai_fight, natureswayofgettingbackatus_fight, bob_fight
    if slim.hp > 0:
        slime_fight()
        if hilichur.hp > 0:
            hilichurl_fight()
            if bigchur.hp > 0:
                bigchurl_fight()
                if abyss_mag.hp > 0:
                    abyssmage_fight()
                    if bandi.hp > 0:
                        bandit_fight()
                        if samura.hp > 0:
                            samurai_fight()
                            if natureswayofgettingbackatu.hp > 0:
                                natureswayofgettingbackatus_fight()
                                if bo.hp > 0:
                                    bob_fight()
else:
    print("You have died because you have no skill l bozo...")










<<<<<<< HEAD
class Battle():
    def Battle_info(enemy):
        print(f"{enemy.name} hp: {enemy.hp}, atk: {enemy.atk}, speed: {enemy.speed}, defense: {enemy.defense}, grass: {enemy.grass}")
        print(f"{first_word} hp: {currentlvl.hp}, atk: {currentlvl.atk}, speed: {currentlvl.speed}, defense: {currentlvl.defense}")
        originalhp = enemy.hp
        originalhpyou = currentlvl.hp
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
            enemy.hp += originalhp
            
=======
>>>>>>> 37347096dc02efa11206b6e52113887664513fad
 





<<<<<<< HEAD
            
        
    
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
    print("grass you have: ")
    print(user.grass)
    print1 = input("This is grass, I know you dont know what it is but you get to touch it for the first time.")
    print2 = input("feels good?")
    print3 = input("bet it doesnt. You havent come out of your moms basement for 31 years.")
    print4 = input("What is wrong with you. 😲")
    print5 = input("Now you fight again UwU")
    Battle.Battle_info(hilichurls)
    user.grass += hilichurls.grass
    print("grass you have: ")
    print(user.grass)
    Battle.Battle_info(bigchurls)
    user.grass += bigchurls.grass
    print("grass you have: ")
    print(user.grass)
    Battle.Battle_info(abyss_mages)
    user.grass += abyss_mages.grass
    print("grass you have: ")
    print(user.grass)
    print5 = input("look what happened")
    currentlvl = lvl2
    print("tada your level2 :D")
    print("you get to shop at the market now! (everybody ran when they saw your face before....)")
    mrkrabs = input("Would you like to go to the market or continue fighting to level up? (Y/N): ").upper()
    if mrkrabs == "Y":
        checker += 1
    elif mrkrabs == "N":
        checker += 2


Merchants()


if checker == 2:
    print("Who do you go to? Robert:")
    Robert = Merchants("Robert", ["the souls of the innocent"])
    user.buy("the souls of the innocent")
    Robert.remove("the souls of the innocent")
    print(user.inventory)
    
=======


>>>>>>> 37347096dc02efa11206b6e52113887664513fad
