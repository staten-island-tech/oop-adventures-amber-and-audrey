class game():
    def __init__(self, name, gender, element, weapon):
        self.name = name
        self.gender = gender
        self.element = element
        self.weapon = weapon
    def __str__(self):
        return f"{self.name}"
    def __str__(self):
        return f"{self.gender}"
    def __str__(self):
        return f"{self.element}"
    def __str__(self):
        return f"{self.weapon}"


Player = []
info = game.create()
player = Player(info)
game.tutorial(player)

print("Hello, ", player.info)

""" class level(game):
    def __init__(self, lvl, hp, atk, speed, defense, quest):
        self.lvl = lvl
        self.hp = hp
        self.atk = atk
        self.speed = speed
        self.defense = defense
        self.quest = quest

level1 = {
        "lvl": 1,
        "hp": 100,
        "atk": 5,
        "speed": 1,
        "defense": 0,
        "quest": [
            "Fight 3 slimes, Fight 3 hilichurls, Fight 1 Bigchurls, Fight 2 Abyss Mages"
        ]
    }

level2 = {
        "lvl": 2,
        "hp": 120,
        "atk": 10,
        "speed": 5,
        "defense": 10,
        "quest": [
            "Fight 10 slimes, Fight 10 hilichurls, Fight 2 Bigchurls, Fight 2 Abyss Mages"
        ]
    }

level3 = {
        "lvl": 3,
        "hp": 140,
        "atk": 20,
        "speed": 10,
        "defense": 20,
        "quest": [
            "Fight 15 slimes, Fight 15 Hilichurls, Fight 3 bigchurls, Fight 3 abyss mages, Fight 4 bandits"
        ]
    }

level4 = {
        "lvl": 4,
        "hp": 160,
        "atk": 30,
        "speed": 20,
        "defense": 30,
        "quest": [
            "Fight 25 slimes, Fight 25 hilichurls, Fight 4 bigchurls, Fight 4 abyss mages, Fight 5 bandits, Fight 1 samurai"
        ]
    }

level5 = {
        "lvl": 5,
        "hp": 180,
        "atk": 50,
        "speed": 30,
        "defense": 40,
        "quest": [
            "Fight 30 slimes, Fight 30 hilichurls, Fight 5 Bigchurls, Fight 5 Abyss Mages, Fight 8 bandits, Fight 2 samurai, fight 3 fatui agents"
        ]
    }

level6 = {
        "lvl": 6,
        "hp": 200,
        "atk": 80,
        "speed": 40,
        "defense": 50,
        "quest": [
            "Fight 46 slimes, Fight 46 hilichurls, Fight 7 Bighchurls, Fight 8 abyss mages, Fight 11 bandits, fight 4 samurai, Fight 4 fatui agents, fight 3 robots"
        ]
    }

level7 = {
        "lvl": 7,
        "hp": 220,
        "atk": 120,
        "speed": 50,
        "defense": 60,
        "quest": [
            "Fight 50 slimes, Fight 50 hilichurls, Fight 9 bigchurls, Fight 9 abyss mages, Fight 14 bandits, Fight 6 samurai, Fight 5 fatui agents, Fight 5 robots"
        ]
    }

level8 = {
        "lvl": 8,
        "hp": 240,
        "atk": 170,
        "speed": 60,
        "defense": 70,
        "quest": [
            "Fight 72 slimes, Fight 75 hilichurls, Fight 10 bigchurls, FIght 15 abyss mages, Fight 16 bandits, Fight 8 samurai, Fight 7 fatui agents, Fight 6 robots, Fight 3 natureswayatgettingbackatus"
        ]
    }

level9 = {
        "lvl": 9,
        "hp": 260,
        "atk": 230,
        "speed": 70,
        "defense": 80,
        "quest": [
            "Fight 80 slimes, Fight 80 hilichurls, Fight 15 bigchurls, Fight 20 abyss mages, Fight 10 samurai, Fight 10 fatui agents, Fight 10 robots, Fight 5 natureswayatgettingbackatus, Fight 1 bob"
        ]
    }

level10 = {
        "lvl": 10,
        "hp": 300,
        "atk": 300,
        "speed": 80,
        "defense": 90,
        "quest": [
            "Fight 100 slimes, Fight 100 hilichurls, Fight 20 Bigchurls, Fight 30 abyss mages, FIght 25 bandits, Fight 15 samurai, Fight 15 fatui agents, Fight 20 robots, Fight 6 natureswayatgettingbackatus, Fight 10 bobs"
        ]
    } """


