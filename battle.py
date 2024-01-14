import random
from classes import user
from classes import enemy
from classes import slime
from classes import hilichurl
from classes import bigchurl
from classes import abyss_mage
from classes import bandit
from classes import samurai
from classes import natureswayofgettingbackatus
from classes import bob

sword = 5
atk = sword

class Battle():
    def slime_fight():
        atk = sword
        slim = slime("Slime", 10, 5, 0, 50)
        player = user("Traveler", 50, 0)
        from operator import add, sub, mul
        while slim.hp > 0:
            print("Your move")
            ops = ("add", "sub", "mul")
            op = random.choice(ops)
            num1, num2 = random.randint(1,12), random.randint(1,12)
            if op == "add":
                print(num1, "+" ,num2)
                mathproblem = num1 + num2
            elif op == "sub":
                print(num1,"-",num2)
                mathproblem = num1 - num2
            elif op == "mul":
                print(num1,"x",num2)
                mathproblem = num1 * num2
            else:
                print("bongo cat")
            mathanswer = int(input("Answer: "))
            if mathanswer == mathproblem:
                slim.hp = slim.hp - atk
                s = input("The slime has taken damage...")
                print(f"Slime hp: {slim.hp}")
                if slim.hp <= 0:
                    print("Traveler has won the battle!")
            else:
                print("Enemies move it move it")
                player.hp = player.hp - slim.atk
                i = input("You took damage...")
                print(f"Your hp: {player.hp}")
                slim.hp = slim.hp - atk
                s = input("The slime has taken damage...")
                print(f"Slime hp: {slim.hp}")
            if player.hp <= 0:
                print("You died...")
                print("You are returning back to the arena to battle again")
                slim.hp = slim.hp
                player.hp = player.hp
                print(f"Your hp: {player.hp}")
                if slim.hp <= 0:
                    print("Traveler has won the battle!")
        player.grass = player.grass + slim.grass
        print(f"Grass obtained: {slim.grass}")
        print1 = input("This is grass, I know you dont know what it is but you get to touch it for the first time.")
        print2 = input("Feels good?")
        print3 = input("Bet it doesnt. You havent come out of your moms basement for 31 years.")
        print4 = input("What is wrong with you. 😲")
        print5 = input("Now you fight again UwU")
    slime_fight()





""" def Battle_info(enemy):
        print(f"{enemy.name} hp: {enemy.hp}, atk: {enemy.atk}, speed: {enemy.speed}, defense: {enemy.defense}, grass: {enemy.grass}")
        print(f"{first_word} hp: {currentlvl.hp}, atk: {currentlvl.atk}, speed: {currentlvl.speed}, defense: {currentlvl.defense}")
        import random
        from operator import add, sub, mul
        while enemy.hp > 0:
            print("your move")
            ops = ("add", "sub", "mul")
            op = random.choice(ops)
            num1, num2 = random.randint(1,12), random.randint(1,12)
            if op == "add":
                print(num1, "+" ,num2)
                mathproblem = num1 + num2
            elif op == "sub":
                print(num1,"-",num2)
                mathproblem = num1 - num2
            elif op == "mul":
                print(num1,"x",num2)
                mathproblem = num1 * num2
            else:
                print("bongo cat")
            mathanswer = int(input("Answer:"))
            print(mathproblem)
            if mathanswer == mathproblem:
                enemy.attack(enemy)
                print(f"enemy hp: {enemy.hp}")
            else:
                print("Enemies move it move it")
                enemy.enemyattack(enemy)
                print(f"your hp:{user.hp}")
        if user.hp == 0:
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
     """