class game():
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


tutorial1 = input("Welcome to Waifu Simulator! Enter a name, gender, element, and weapon: ")

name = game("", "", "", "", "")
gender = game("", "", "", "", "")
element = game("", "", "", "", "")
weapon = game("", "", "", "", "")

info = game(name, gender, element, weapon, tutorial1)

if (",") in tutorial1:
    print("Hello, ", info)
if not tutorial1:
    print("Sorry there is no info found.")




class level(game):
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


print()
print("You are level 1 because you repel women lmao.")

tutorial2 = input("Would you like to see your stats for level 1? (Y/N): ")

if tutorial2 == "Y":
    print(level.lvl1[0])
else:
    print("...")

tutorial3 = input("Would you like to see your currently available quests? (Y/N): ")

if tutorial3 == "Y":
    print(lvl1[5])
else:
    print("Bruh you coward.")
