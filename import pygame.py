import random

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
    damage = random.randint(20, 30)
    target.health -= damage
    print(f"Inflation loses {damage} health due to the Audit Smash!")

def inflation_special_ability(target):
    print("Inflation uses Price Surge!")
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
        print("Inflation, the ever-present antagonist, looms over the city.\n")

    def dialogue(self):
        dialogues = [
            "Craig: Time to balance the books, Inflation!",
            "Inflation: You can't audit me, Craig. I'm everywhere!",
            "Craig: Let's see if your numbers add up!",
            "Inflation: You'll need more than a calculator to defeat me!",
            "Craig: Your economic policies end tonight, Inflation!",
            "Inflation: Haha, Craig! You're just a tiny blip in my financial plans!"
        ]
        print(random.choice(dialogues))

    def fight(self):
        while not self.craig.is_defeated() and not self.inflation.is_defeated():
            self.dialogue()

            if random.random() < 0.2:  # 20% chance for special ability
                craig_special_ability(self.inflation)
            else:
                damage = random.randint(5, 15)
                self.inflation.health -= damage
                print(f"Craig attacks! Inflation loses {damage} health.")

            if self.inflation.is_defeated():
                print("Inflation is defeated! The city's economy stabilizes!")
                break

            if random.random() < 0.2:  # 20% chance for special ability
                inflation_special_ability(self.craig)
            else:
                damage = random.randint(5, 15)
                self.craig.health -= damage
                print(f"Inflation strikes back! Craig loses {damage} health.")

            if self.craig.is_defeated():
                print("Craig is defeated! Fiscal chaos reigns!")
                break

            if random.random() < 0.1:  # 10% chance for random event
                self.random_event()

    def random_event(self):
        events = [
            "A mysterious benefactor drops a health potion for Craig!",
            "Inflation's influence wanes momentarily, reducing its attack power!"
        ]
        event = random.choice(events)
        print(event)
        if "health potion" in event:
            self.craig.inventory.append(20)  # Adds 20 health potion
        elif "reducing its attack power" in event:
            inflation_special_ability(self.craig)  # Reduces the effect of Inflation's next attack

# Creating characters
craig = Character("Craig", 100)
inflation = Character("Inflation", 100)

# Starting the game
game = GameStage(craig, inflation)
game.introduction()
game.fight()
