from classes import user, slime, hilichurl, bigchurl, abyss_mage, bandit, samurai, natureswayofgettingbackatus, bob
from battle import slime_fight, hilichurl_fight


#player
player = user("Traveler", 100, 0)

#enemies
slim = slime("Slime", 10, 5, 20)
hilichur = hilichurl("Hilichurl", 30, 5, 40)
bigchur = bigchurl("Bigchurl", 50, 10, 60)
abyss_mag = abyss_mage("Abyss Mage", 70, 10, 80)
bandi = bandit("Bandit", 90, 15, 100)
samura = samurai("Samurai", 110, 15, 120)
natureswayofgettingbackatu = natureswayofgettingbackatus("Natureswayofgettingbackatu", 130, 20, 140)
bo = bob("bob", 150, 30, 400)

#start of game     
print("Welcome to Waifu Simulator!")
print()
name = input("What is your name? ")
print("Hello,", name)
tut1 = input("This journey is going to be a tough one, but you will be rewarded generously... With grass of course :)")
tut2 = input("You'll start off with a wooden sword, but after you defeat a slime, you can access the Merchant Shop to upgrade your gear.")
tut3 = input("Anyways, enough talking and get into action!")
tut4 = input("You are now walking towards the battle arena...")
print()
#slime fight
tut5 = input("You have encountered a slime!!")
if player.hp > 0:
    if slim.hp > 0:
        slime_fight()
        from merchants import merchant_shop
        Robert = merchant_shop("Robert", {"stone sword (cost: 20 grass; atk: 7)", "iron sword (cost: 40 grass; atk: 10)", "gold sword (cost: 60 grass; atk: 13)", "diamond sword (cost: 80 grass; atk: 15)", "emerald sword (cost: 100 grass; atk: 18)", "netherite sword (cost: 120 grass; atk: 20)", "ultimate sword (cost: 140 grass; atk: 25)"})
        merchant_shop(Robert)
        if hilichur.hp > 0:
            hilichurl_fight()



#unlocks merchant shop










 







