import random
import time
import sys

def slow_typing(text, speed=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

# ASCII Art for the game title
game_title_art = """ 
████████████████████████████████████████████████████████████████████████████████████████████
█─▄▄▄─█─▄▄─█─▄▄▄▄█─▄─▄─███─▄▄─█▄─▄▄─███▄─▄█▄─▀█▄─▄█▄─▄▄─█▄─▄████▀▄─██─▄─▄─█▄─▄█─▄▄─█▄─▀█▄─▄█
█─███▀█─██─█▄▄▄▄─███─█████─██─██─▄██████─███─█▄▀─███─▄████─██▀██─▀─████─████─██─██─██─█▄▀─██
▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀▀▀▄▄▄▄▀▄▄▄▀▀▀▀▀▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀▀▄▄▄▀▀▄▄▄▀▄▄▄▄▀▄▄▄▀▀▄▄▀
                                                                      
"""

# ASCII Art for characters
craig_art = """
  C
 /|\\
 / \\
"""
inflation_art = """
   __
  /  \\
 |    |
  \\__/
"""

class Character:
    def __init__(self, name, health, art):
        self.name = name
        self.health = health
        self.art = art
        self.inventory = []

    def is_defeated(self):
        return self.health <= 0

    def use_item(self):
        if self.inventory:
            item = self.inventory.pop()
            self.health += item
            slow_typing(f"{self.name} uses a health potion and recovers {item} health!")
            time.sleep(1)
            slow_typing(random.choice(self.item_use_dialogues()))
        else:
            slow_typing(f"{self.name} has no items to use.")

    def item_use_dialogues(self):
        return [
            "Craig: A little boost never hurts!",
            "Craig: Time for a quick recharge!",
            "Craig: Back in the fight!"
        ]

def craig_special_ability(target):
    slow_typing("Craig uses his Audit Smash!")
    time.sleep(1)
    damage = random.randint(20, 30)
    target.health -= damage
    slow_typing(f"Inflation loses {damage} health due to the Audit Smash!")
    slow_typing(random.choice(craig_special_ability_dialogues()))

def craig_special_ability_dialogues():
    return [
        "Craig: Take that, Inflation!",
        "Craig: Audit Smash, for fiscal responsibility!",
        "Craig: This will leave a dent in your budget!"
    ]

def inflation_special_ability(target):
    slow_typing("Inflation uses Price Surge!")
    time.sleep(1)
    damage = random.randint(20, 30)
    target.health -= damage
    slow_typing(f"Craig loses {damage} health due to the Price Surge!")
    slow_typing(random.choice(inflation_special_ability_dialogues()))

def inflation_special_ability_dialogues():
    return [
        "Inflation: Feel the power of rising prices!",
        "Inflation: This surge will destabilize your assets!",
        "Inflation: Economic chaos is my game!"
    ]

class GameStage:
    def __init__(self, craig, inflation):
        self.craig = craig
        self.inflation = inflation

    def introduction(self):
        slow_typing("Craig, tired of his dead-end accounting job, becomes a vigilante at night.")
        time.sleep(2)
        slow_typing("Inflation, the ever-present antagonist, looms over the city.\n")
        time.sleep(2)
        slow_typing(craig_art)
        slow_typing(inflation_art)
        time.sleep(2)

    def fight(self):
        while not self.craig.is_defeated() and not self.inflation.is_defeated():
            self.player_choice()
            time.sleep(1)
            self.inflation_turn()
            time.sleep(2)

    def player_choice(self):
        slow_typing("\nChoose your action:")
        slow_typing("1. Attack")
        slow_typing("2. Use Special Ability")
        slow_typing("3. Use Item")
        choice = input("Enter your choice (1, 2, or 3): ")
        time.sleep(1)

        if choice == "1":
            damage = random.randint(5, 15)
            self.inflation.health -= damage
            slow_typing(f"Craig attacks! Inflation loses {damage} health.")
            slow_typing(random.choice(attack_dialogues()))
        elif choice == "2":
            craig_special_ability(self.inflation)
        elif choice == "3":
            self.craig.use_item()
        else:
            slow_typing("Invalid choice. Craig hesitates...")
        time.sleep(1)

    def inflation_turn(self):
        if self.inflation.is_defeated():
            slow_typing("Inflation is defeated! The city's economy stabilizes!")
            return

        if random.random() < 0.2:
            inflation_special_ability(self.craig)
        else:
            damage = random.randint(5, 15)
            self.craig.health -= damage
            slow_typing(f"Inflation strikes back! Craig loses {damage} health.")
            slow_typing(random.choice(inflation_attack_dialogues()))

        if self.craig.is_defeated():
            slow_typing("Craig is defeated! Fiscal chaos reigns!")
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
craig = Character("Craig", 100, craig_art)
inflation = Character("Inflation", 100, inflation_art)

# Starting the game
slow_typing(game_title_art)
game = GameStage(craig, inflation)
game.introduction()
game.fight()
