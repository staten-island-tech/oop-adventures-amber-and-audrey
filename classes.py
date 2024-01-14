#user class for the player
class user():
    def __init__(self, name, hp, grass):
        self.name = name
        self.hp = int(hp)
        self.grass = int(grass)
    def __str__(self):
        tutorial = input("What is your name?")
        return f"{self.name}, {self.hp}, {self.grass}"

player = user("Traveler", 50, 0)
"""     def buy(item):
        user.inventory.append(item)
        user.inventory.remove.grass(item) """

#enemy class in the game class to set, name, hp, atk, def, of each enemy
class enemy():
    def __init__(self, name):
        self.name = name

class slime(enemy):
    def __init__(self, name, hp, atk, defense, grass):
        super().__init__(name)
        self.hp = int(hp)
        self.atk = int(atk)
        self.defense = int(defense)
        self.grass = int(grass)
    def __str__(self):
        return f"{self.name}, {self.hp}, {self.atk}, {self.defense}, {self.grass}"

class hilichurl(slime):
    def __init__(self, name, hp, atk, defense, grass):
        super().__init__(name, hp, atk, defense, grass)
        def __str__(self):
            return f"{self.name}, {self.hp}, {self.atk}, {self.defense}, {self.grass}"

class bigchurl(slime):
    def __init__(self, name, hp, atk, defense, grass):
        super().__init__(name, hp, atk, defense, grass)
        def __str__(self):
            return f"{self.name}, {self.hp}, {self.atk}, {self.defense}, {self.grass}"

class abyss_mage(slime):
    def __init__(self, name, hp, atk, defense, grass):
        super().__init__(name, hp, atk, defense, grass)
        def __str__(self):
            return f"{self.name}, {self.hp}, {self.atk}, {self.defense}, {self.grass}"

class bandit(slime):
    def __init__(self, name, hp, atk, defense, grass):
        super().__init__(name, hp, atk, defense, grass)
        def __str__(self):
            return f"{self.name}, {self.hp}, {self.atk}, {self.defense}, {self.grass}"

class samurai(slime):
    def __init__(self, name, hp, atk, defense, grass):
        super().__init__(name, hp, atk, defense, grass)
        def __str__(self):
            return f"{self.name}, {self.hp}, {self.atk}, {self.defense}, {self.grass}"

class natureswayofgettingbackatus(slime):
    def __init__(self, name, hp, atk, defense, grass):
        super().__init__(name, hp, atk, defense, grass)
        def __str__(self):
            return f"{self.name}, {self.hp}, {self.atk}, {self.defense}, {self.grass}"

class bob(slime):
    def __init__(self, name, hp, atk, defense, grass):
        super().__init__(name, hp, atk, defense, grass)
        def __str__(self):
            return f"{self.name}, {self.hp}, {self.atk}, {self.defense}, {self.grass}"





"""     def attack(self, enemies):
        enemies.hp = enemies.hp - currentlvl.atk
    def enemyattack(self, enemies):
        currentlvl.hp = currentlvl.hp - enemies.atk """