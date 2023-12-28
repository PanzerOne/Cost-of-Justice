import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FONT_SIZE = 24
FPS = 30

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define the main character class
class Character:
    def __init__(self, name, age, job, happiness):
        self.name = name
        self.age = age
        self.job = job
        self.happiness = happiness

    def change_job(self, new_job):
        self.job = new_job

    def boost_happiness(self):
        self.happiness += random.randint(1, 5)

# define the Antagonist Class 
class Antagonist:
    def __init__(self,name,strength,influence):
        self.name = name
        self.strength = strength
        self.influence = influence

    def increase_strength(self):
        self.strength += random.randint(1,3)

    def weaken(self, amount):
        self.strength -= amount
        if self.strength < 0:
            self.strength = 0

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cost of Justice")

# Initialize font
font = pygame.font.Font(None, FONT_SIZE)

# Create a character
player = Character("Craig", 38, "Accountant", 50)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    screen.fill(WHITE)

    # Display character information
    info_text = f"Name: {player.name}, Age: {player.age}, Job: {player.job}, Happiness: {player.happiness}"
    text_render = font.render(info_text, True, BLACK)
    screen.blit(text_render, (20, 20))

    # Display game instructions and options
    instructions = "Choose an action:\n1 - Change Job\n2 - Fight Inflation\n3 - Go on Vacation\n4 - Quit"
    instructions_render = font.render(instructions, True, BLACK)
    screen.blit(instructions_render, (20, 60))

    pygame.display.flip()

    action = input("You have to take a decision!! What you going to do chico?: ")

    if action == '1':
        new_job = input("Enter your new job: ")
        player.change_job(new_job)
        player.boost_happiness()
        print(f"You are now a {new_job}. Your happiness increased!Enjoy the temporary high")
    elif action == '2':
        inflation_damage = random.randint(10, 30)
        player.happiness -= inflation_damage
        print(f"You tried to fight Inflation but lost {inflation_damage} happiness points!")
    elif action == '3':
        vacation_days = random.randint(1, 7)
        player.happiness += vacation_days * 5
        print(f"You went on vacation for {vacation_days} days and returned happier!")
    elif action == '4':
        print("Thanks for playing!You Quit like everything else you do!")
        running = False
    else:
        print("Invalid choice. Please choose a valid option.")

    if player.happiness <= 0:
        print("You're too unhappy to continue. Game over!")
        running = False

    pygame.time.delay(1000)

pygame.quit()
sys.exit()