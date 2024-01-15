import random
from classes import user
from classes import slime
from classes import hilichurl
from classes import bigchurl
from classes import abyss_mage
from classes import bandit
from classes import samurai
from classes import natureswayofgettingbackatus
from classes import bob


wooden_sword = 5
atk = wooden_sword

def slime_fight():
    atk = wooden_sword
    slim = slime("Slime", 10, 5, 20)
    player = user("Traveler", 100, 0)
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
    print5 = input("Now you'll go redirect to the Merchant Shop where you can upgrade your gear")
    print()


def hilichurl_fight():
    player = user("Traveler", 100, 0)
    hilichur = hilichurl("Hilichurl", 30, 5, 40)
    stone_sword = 7
    atk = stone_sword
    from operator import add, sub, mul
    while hilichur.hp > 0:
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
            hilichur.hp = hilichur.hp - atk
            s = input("The hilichurl has taken damage...")
            print(f"Hilichurl hp: {hilichur.hp}")
            if hilichur.hp <= 0:
                print("Traveler has won the battle!")
            else:
                print("Enemies move it move it")
                player.hp = player.hp - hilichur.atk
                i = input("You have taken damage...")
                print(f"Your hp: {player.hp}")
                hilichur.hp = hilichur.hp - atk
                s = input("The hilichurl has taken damage...")
                print(f"Hilichurl hp: {hilichur.hp}")
            if player.hp <= 0:
                print("You died...")
                print("You are returning back to the arena to battle again")
                hilichur.hp = hilichur.hp
                player.hp = player.hp
                print(f"Your hp: {player.hp}")
                if hilichur.hp <= 0:
                    print("Traveler has won the battle!")
    player.grass = player.grass + hilichur.grass
    print(f"Grass obtained: {hilichur.grass}")
    print6 = input("I see you are getting the hang of it...")
    print7 = input("I'll just have to make it more challenging... But first the shop :)")









