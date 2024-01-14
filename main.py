from battle import Battle
from classes import user, enemy, slime, hilichurl, bigchurl, abyss_mage, bandit, samurai, natureswayofgettingbackatus, bob

#start currency amount
grass = 0
user.grass = grass
user.inventory.append(grass)




#start of game     
print("Welcome to Waifu Simulator!")
print()
name = input("What is your name?")
print("Hello,", name)
a = input("This journey is going to be a tough one, but you will be rewarded generously... With grass of course :)")
#player
player = user(name, 50)
#enemies
slim = slime("Slime", 10, 5, 0, 50)
hilichur = hilichurl("hilichurls", 20, 5, 5, 100)
bigchur = bigchurl("bigchurls", 30, 10, 10, 150)
abyss_mag = abyss_mage("abyss_mages", 40, 10, 10, 200)
bandi = bandit("bandits", 50, 15, 15, 250)
samura = samurai("samurais", 60, 15, 15, 300)
natureswayofgettingbackatu = natureswayofgettingbackatus("natureswayofgettingbackatus", 70, 20, 20, 350)
bo = bob("bob", 80, 30, 30, 400)

