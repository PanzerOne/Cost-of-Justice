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
        else:
            print(f"{self.name} has no items to use.")

# Special Abilities
def craig_special_ability(target):
    print("Craig uses his Audit Smash!")
    time.sleep(1)
    damage = random.randint(20, 30)
    target.health -= damage
    print(f"Inflation loses {damage} health due to the Audit Smash!")

def inflation_special_ability(target):
    print("Inflation uses Price Surge!")
    time.sleep(1)
    damage = random.randint(20, 30)
    target.health -= damage
    print(f"Craig loses {damage} health due to the Price Surge!")

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

    def dialogue(self):
        dialogues = [
            # ... (existing dialogues)
        ]
        print(random.choice(dialogues))
        time.sleep(2)

    def fight(self):
        while not self.craig.is_defeated() and not self.inflation.is_defeated():
            self.dialogue()
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

        if self.craig.is_defeated():
            print("Craig is defeated! Fiscal chaos reigns!")
        time.sleep(1)

    def random_event(self):
        # ... (existing random event code)
        time.sleep(1)

# Creating characters
craig = Character("Craig", 100)
inflation = Character("Inflation", 100)

# Starting the game
game = GameStage(craig, inflation)
game.introduction()
game.fight()

