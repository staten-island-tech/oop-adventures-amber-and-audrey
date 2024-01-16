from classes import user, slime, hilichurl, bigchurl, abyss_mage, bandit, samurai, natureswayofgettingbackatus, bob


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