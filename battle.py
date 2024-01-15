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
    slim = slime("Slime", 10, 5)
    player = user("Traveler", 100)
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
    print1 = input("This is grass, I know you dont know what it is but you get to touch it for the first time.")
    print2 = input("Feels good?")
    print3 = input("Bet it doesnt. You havent come out of your moms basement for 31 years.")
    print4 = input("What is wrong with you. 😲")
    print5 = input("Now you'll have to battle again, but this time with a better weapon: stone sword")
    print()
slime_fight()



def hilichurl_fight():
    player = user("Traveler", 100)
    hilichur = hilichurl("Hilichurl", 30, 5)
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
    print6 = input("I see you are getting the hang of it...")
    print7 = input("I'll just have to make it more challenging...")
    print()
hilichurl_fight()

def bigchurl_fight():
    player = user("Traveler", 100)
    bigchur = bigchurl("Hilichurl", 30, 5)
    iron_sword = 10
    atk = iron_sword
    from operator import add, sub, mul
    while bigchur.hp > 0:
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
            bigchur.hp = bigchur.hp - atk
            s = input("The bigchurl has taken damage...")
            print(f"Bigchurl hp: {bigchur.hp}")
            if bigchur.hp <= 0:
                print("Traveler has won the battle!")
            else:
                print("Enemies move it move it")
                player.hp = player.hp - bigchur.atk
                i = input("You have taken damage...")
                print(f"Your hp: {player.hp}")
                bigchur.hp = bigchur.hp - atk
                s = input("The bigchurl has taken damage...")
                print(f"Bigchurl hp: {bigchur.hp}")
            if player.hp <= 0:
                print("You died...")
                print("You are returning back to the arena to battle again")
                bigchur.hp = bigchur.hp
                player.hp = player.hp
                print(f"Your hp: {player.hp}")
                if bigchur.hp <= 0:
                    print("Traveler has won the battle!")
    print("Traveler has won the battle!")                
    print9 = input("Hmm, I guess this was not much of a challenge huh...")
    print10 = input("You'll now be using a gold sword cause the next enemy is gonna be harder... Be ready and brace yourself")
    print()
bigchurl_fight()

def abyssmage_fight():
    player = user("Traveler", 100)
    abyss_mag = abyss_mage("Abyss Mage", 70, 10)
    gold_sword = 15
    atk = gold_sword
    from operator import add, sub, mul
    while abyss_mag.hp > 0:
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
            abyss_mag.hp = abyss_mag.hp - atk
            s = input("The abyss mage has taken damage...")
            print(f"Bigchurl hp: {abyss_mag.hp}")
            if abyss_mag.hp <= 0:
                print("Traveler has won the battle!")
            else:
                print("Enemies move it move it")
                player.hp = player.hp - abyss_mag.atk
                i = input("You have taken damage...")
                print(f"Your hp: {player.hp}")
                abyss_mag.hp = abyss_mag.hp - atk
                s = input("The abyss mage has taken damage...")
                print(f"Abyss Mage hp: {abyss_mag.hp}")
            if player.hp <= 0:
                print("You died...")
                print("You are returning back to the arena to battle again")
                abyss_mag.hp = abyss_mag.hp
                player.hp = player.hp
                print(f"Your hp: {player.hp}")
                if abyss_mag.hp <= 0:
                    print("Traveler has won the battle!")
    print11 = input("Wow, I see that you have been paying attention to math class")
    print12 = input("Maybe you've gotten used to touching grass... Afterall, you've fought 4 enemies already")
    print13 = input("You'll now fight the next enemy with a diamond sword, hopefully you won't die :D")
    print()
abyssmage_fight()

def bandit_fight():
    player = user("Traveler", 100)
    bandi = bandit("Bandit", 90, 15)
    diamond_sword = 18
    atk = diamond_sword
    from operator import add, sub, mul
    while bandi.hp > 0:
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
            bandi.hp = bandi.hp - atk
            s = input("The bandit has taken damage...")
            print(f"Bandit hp: {bandi.hp}")
            if bandi.hp <= 0:
                print("Traveler has won the battle!")
            else:
                print("Enemies move it move it")
                player.hp = player.hp - bandi.atk
                i = input("You have taken damage...")
                print(f"Your hp: {player.hp}")
                bandi.hp = bandi.hp - atk
                s = input("The samurai has taken damage...")
                print(f"Bandit hp: {bandi.hp}")
            if player.hp <= 0:
                print("You died...")
                print("You are returning back to the arena to battle again")
                bandi.hp = bandi.hp
                player.hp = player.hp
                print(f"Your hp: {player.hp}")
                if bandi.hp <= 0:
                    print("Traveler has won the battle!")
    print14 = input("")
    
    print()
bandit_fight()

def samurai_fight():
    player = user("Traveler", 100)
    samura = samurai("Samurai", 110, 15)
    emerald_sword = 20
    atk = emerald_sword
    from operator import add, sub, mul
    while samura.hp > 0:
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
            samura.hp = samura.hp - atk
            s = input("The samurai has taken damage...")
            print(f"Samurai hp: {samura.hp}")
            if samura.hp <= 0:
                print("Traveler has won the battle!")
            else:
                print("Enemies move it move it")
                player.hp = player.hp - samura.atk
                i = input("You have taken damage...")
                print(f"Your hp: {player.hp}")
                samura.hp = samura.hp - atk
                s = input("The samurai has taken damage...")
                print(f"Samurai hp: {samura.hp}")
            if player.hp <= 0:
                print("You died...")
                print("You are returning back to the arena to battle again")
                samura.hp = samura.hp
                player.hp = player.hp
                print(f"Your hp: {player.hp}")
                if samura.hp <= 0:
                    print("Traveler has won the battle!")
    
    
    
    print()
samurai_fight()

def natureswayofgettingbackatus_fight():
    player = user("Traveler", 100)
    natureswayofgettingbackatu = natureswayofgettingbackatus("Natureswayofgettingbackatu", 130, 20)
    netherite_sword = 25
    atk = netherite_sword
    from operator import add, sub, mul
    while natureswayofgettingbackatu.hp > 0:
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
            natureswayofgettingbackatu.hp = natureswayofgettingbackatu.hp - atk
            s = input("The natureswayofgettingbackatus has taken damage...")
            print(f"Natureswayofgettingbackatus hp: {natureswayofgettingbackatu.hp}")
            if natureswayofgettingbackatu.hp <= 0:
                print("Traveler has won the battle!")
            else:
                print("Enemies move it move it")
                player.hp = player.hp - natureswayofgettingbackatu.atk
                i = input("You have taken damage...")
                print(f"Your hp: {player.hp}")
                natureswayofgettingbackatu.hp = natureswayofgettingbackatu.hp - atk
                s = input("The natureswayofgettingbackatus has taken damage...")
                print(f"Natureswayofgettingbackatus hp: {natureswayofgettingbackatu.hp}")
            if player.hp <= 0:
                print("You died...")
                print("You are returning back to the arena to battle again")
                natureswayofgettingbackatu.hp = natureswayofgettingbackatu.hp
                player.hp = player.hp
                print(f"Your hp: {player.hp}")
                if natureswayofgettingbackatu.hp <= 0:
                    print("Traveler has won the battle!")
    
    
    
    print()
natureswayofgettingbackatus_fight()

def bob_fight():
    player = user("Traveler", 100)
    bo = bob("bob", 150, 25)
    ultimate_sword = 30
    atk = ultimate_sword
    from operator import add, sub, mul
    while bo.hp > 0:
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
            bo.hp = bo.hp - atk
            s = input("BOB has taken damage...")
            print(f"bob hp: {bo.hp}")
            if bo.hp <= 0:
                print("Traveler has won the battle!")
            else:
                print("Enemies move it move it")
                player.hp = player.hp - bo.atk
                i = input("You have taken damage...")
                print(f"Your hp: {player.hp}")
                bo.hp = bo.hp - atk
                s = input("The natureswayofgettingbackatus has taken damage...")
                print(f"bob hp: {bo.hp}")
            if player.hp <= 0:
                print("You died...")
                print("You are returning back to the arena to battle again")
                bo.hp = bo.hp
                player.hp = player.hp
                print(f"Your hp: {player.hp}")
                if bo.hp <= 0:
                    print("Traveler has won the battle!")
    
    
    
    print()
bob_fight()