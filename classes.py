#user class for the player
class user():
    def __init__(self, name, hp):
        self.name = name
        self.hp = int(hp)
    def __str__(self):
        tutorial = input("What is your name?")
        return f"{self.name}, {self.hp}, {self.atk}"

player = user("Traveler", 100)


#enemy class in the game class to set, name, hp, atk, def, of each enemy
class enemy():
    def __init__(self, name):
        self.name = name

class slime(enemy):
    def __init__(self, name, hp, atk):
        super().__init__(name)
        self.hp = int(hp)
        self.atk = int(atk)
    def __str__(self):
        return f"{self.name}, {self.hp}, {self.atk}"

class hilichurl(slime):
    def __init__(self, name, hp, atk):
        super().__init__(name, hp, atk)
        def __str__(self):
            return f"{self.name}, {self.hp}, {self.atk}"

class bigchurl(slime):
    def __init__(self, name, hp, atk):
        super().__init__(name, hp, atk)
        def __str__(self):
            return f"{self.name}, {self.hp}, {self.atk}"

class abyss_mage(slime):
    def __init__(self, name, hp, atk):
        super().__init__(name, hp, atk)
        def __str__(self):
            return f"{self.name}, {self.hp}, {self.atk}"

class bandit(slime):
    def __init__(self, name, hp, atk):
        super().__init__(name, hp, atk)
        def __str__(self):
            return f"{self.name}, {self.hp}, {self.atk}"

class samurai(slime):
    def __init__(self, name, hp, atk):
        super().__init__(name, hp, atk)
        def __str__(self):
            return f"{self.name}, {self.hp}, {self.atk}"

class natureswayofgettingbackatus(slime):
    def __init__(self, name, hp, atk):
        super().__init__(name, hp, atk)
        def __str__(self):
            return f"{self.name}, {self.hp}, {self.atk}"

class bob(slime):
    def __init__(self, name, hp, atk):
        super().__init__(name, hp, atk)
        def __str__(self):
            return f"{self.name}, {self.hp}, {self.atk}"

