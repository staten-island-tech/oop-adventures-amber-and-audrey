from classes import user


class merchant_shop():
    def __init__(self, name, products):
        self.name = name
        self.products = products
        tut7 = input("Welcome to my shop!")
        print(products)
        tut8 = input("What would you like to buy from the shop? ")
        if "stone sword":
            player.grass = player.grass - 20
            print(f"Grass left: {player.grass}")
            print("You have equipped a stone sword! Come test it out on the new enemy: Hilichurl")
            print("Walking to the battle arena...")
            print()
        elif "iron sword":
            player.grass = player.grass - 40
            print(f"Grass left: {player.grass}")
            print("You have equipped an iron sword! Come test it out on the new enemy: Bigchurl")
            print("Walking to the battle arena...")
            print()
        elif "gold sword":
            player.grass = player.grass - 60
            print(f"Grass left: {player.grass}")
            print("You have equipped a gold sword! Come test it out on the new enemy: Abyss Mage")
            print("Walking to the battle arena...")
            print()
        elif "diamond sword":
            player.grass = player.grass - 80
            print(f"Grass left: {player.grass}")
            print("You have equipped a diamond sword! Come test it out on the new enemy: Bandit")
            print("Walking to the battle arena...")
            print()
        elif "emerald sword":
            player.grass = player.grass - 100
            print(f"Grass left: {player.grass}")
            print("You have equipped an emerald sword! Come test it out on the new enemy: Samurai")
            print("Walking to the battle arena...")
            print()
        elif "netherite sword":
            player.grass = player.grass - 120
            print(f"Grass left: {player.grass}")
            print("You have equipped a netherite sword! Come test it out on the new enemy: Natureswayatgettingbackatus")
            print("Walking to the battle arena...")
            print()
        elif "ultimate sword":
            player.grass = player.grass - 140
            print(f"Grass left: {player.grass}")
            print("You have equipped the ultimate sword! Come test it out on the final boss: BOB")
            print("Walking to the battle arena...")
            print()
        else:
            print("erm i think you misspelled...")

player = user("Traveler", 100, 0)      
Robert = merchant_shop("Robert", {"stone sword (cost: 20 grass; atk: 7)", "iron sword (cost: 40 grass; atk: 10)", "gold sword (cost: 60 grass; atk: 13)", "diamond sword (cost: 80 grass; atk: 15)", "emerald sword (cost: 100 grass; atk: 18)", "netherite sword (cost: 120 grass; atk: 20)", "ultimate sword (cost: 140 grass; atk: 25)"})





    

                 