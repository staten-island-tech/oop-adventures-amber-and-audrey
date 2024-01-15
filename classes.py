#user class for the player
class user():
    def __init__(self, name, hp, grass):
        self.name = name
        self.hp = int(hp)
        self.grass = int(grass)
    def __str__(self):
        tutorial = input("What is your name?")
        return f"{self.name}, {self.hp}, {self.atk}, {self.grass}"

player = user("Traveler", 100, 0)


#enemy class in the game class to set, name, hp, atk, def, of each enemy
class enemy():
    def __init__(self, name):
        self.name = name

class slime(enemy):
    def __init__(self, name, hp, atk, grass):
        super().__init__(name)
        self.hp = int(hp)
        self.atk = int(atk)
        self.grass = int(grass)
    def __str__(self):
        return f"{self.name}, {self.hp}, {self.atk}, {self.grass}"

class hilichurl(slime):
    def __init__(self, name, hp, atk, grass):
        super().__init__(name, hp, atk, grass)
        def __str__(self):
            return f"{self.name}, {self.hp}, {self.atk}, {self.grass}"

class bigchurl(slime):
    def __init__(self, name, hp, atk, grass):
        super().__init__(name, hp, atk, grass)
        def __str__(self):
            return f"{self.name}, {self.hp}, {self.atk}, {self.grass}"

class abyss_mage(slime):
    def __init__(self, name, hp, atk, grass):
        super().__init__(name, hp, atk, grass)
        def __str__(self):
            return f"{self.name}, {self.hp}, {self.atk}, {self.grass}"

class bandit(slime):
    def __init__(self, name, hp, atk, grass):
        super().__init__(name, hp, atk, grass)
        def __str__(self):
            return f"{self.name}, {self.hp}, {self.atk}, {self.grass}"

class samurai(slime):
    def __init__(self, name, hp, atk, grass):
        super().__init__(name, hp, atk, grass)
        def __str__(self):
            return f"{self.name}, {self.hp}, {self.atk}, {self.grass}"

class natureswayofgettingbackatus(slime):
    def __init__(self, name, hp, atk, grass):
        super().__init__(name, hp, atk, grass)
        def __str__(self):
            return f"{self.name}, {self.hp}, {self.atk}, {self.grass}"

class bob(slime):
    def __init__(self, name, hp, atk, grass):
        super().__init__(name, hp, atk, grass)
        def __str__(self):
            return f"{self.name}, {self.hp}, {self.atk}, {self.grass}"

