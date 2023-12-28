import random
import time

# Class for the game character
class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.inventory = []

    def is_defeated(self):
        return self.health <= 0

    def use_item(self):
        if self.inventory:
            item = self.inventory.pop()
            self.health += item
            print(f"{self.name} uses a health potion and recovers {item} health!")
            time.sleep(1)
            print(random.choice(self.item_use_dialogues()))
        else:
            print(f"{self.name} has no items to use.")

    def item_use_dialogues(self):
        return [
            "Craig: A little boost never hurts!",
            "Craig: Time for a quick recharge!",
            "Craig: Back in the fight!"
        ]

# Special Abilities
def craig_special_ability(target):
    print("Craig uses his Audit Smash!")
    time.sleep(1)
    damage = random.randint(20, 30)
    target.health -= damage
    print(f"Inflation loses {damage} health due to the Audit Smash!")
    print(random.choice(craig_special_ability_dialogues()))

def craig_special_ability_dialogues():
    return [
        "Craig: Take that, Inflation!",
        "Craig: Audit Smash, for fiscal responsibility!",
        "Craig: This will leave a dent in your budget!"
    ]

def inflation_special_ability(target):
    print("Inflation uses Price Surge!")
    time.sleep(1)
    damage = random.randint(20, 30)
    target.health -= damage
    print(f"Craig loses {damage} health due to the Price Surge!")
    print(random.choice(inflation_special_ability_dialogues()))

def inflation_special_ability_dialogues():
    return [
        "Inflation: Feel the power of rising prices!",
        "Inflation: This surge will destabilize your assets!",
        "Inflation: Economic chaos is my game!"
    ]

# Class for the game stages
class GameStage:
    def __init__(self, craig, inflation):
        self.craig = craig
        self.inflation = inflation

    def introduction(self):
        print("Craig, tired of his dead-end accounting job, becomes a vigilante at night.")
        time.sleep(2)
        print("Inflation, the ever-present antagonist, looms over the city.\n")
        time.sleep(2)

    def fight(self):
        while not self.craig.is_defeated() and not self.inflation.is_defeated():
            self.player_choice()
            time.sleep(1)
            self.inflation_turn()
            time.sleep(2)

    def player_choice(self):
        print("\nChoose your action:")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Use Item")
        choice = input("Enter your choice (1, 2, or 3): ")
        time.sleep(1)

        if choice == "1":
            damage = random.randint(5, 15)
            self.inflation.health -= damage
            print(f"Craig attacks! Inflation loses {damage} health.")
            print(random.choice(attack_dialogues()))
        elif choice == "2":
            craig_special_ability(self.inflation)
        elif choice == "3":
            self.craig.use_item()
        else:
            print("Invalid choice. Craig hesitates...")
        time.sleep(1)

    def inflation_turn(self):
        if self.inflation.is_defeated():
            print("Inflation is defeated! The city's economy stabilizes!")
            return

        if random.random() < 0.2:
            inflation_special_ability(self.craig)
        else:
            damage = random.randint(5, 15)
            self.craig.health -= damage
            print(f"Inflation strikes back! Craig loses {damage} health.")
            print(random.choice(inflation_attack_dialogues()))

        if self.craig.is_defeated():
            print("Craig is defeated! Fiscal chaos reigns!")
        time.sleep(1)

def attack_dialogues():
    return [
        "Craig: Take that!",
        "Craig: How's that for accounting!",
        "Craig: You can't escape justice!"
    ]

def inflation_attack_dialogues():
    return [
        "Inflation: You can't stop the economic tide!",
        "Inflation: My power grows with every strike!",
        "Inflation: You're no match for market forces!"
    ]

# Creating characters
craig = Character("Craig", 100)
inflation = Character("Inflation", 100)

# Starting the game
game = GameStage(craig, inflation)
game.introduction()
game.fight()
