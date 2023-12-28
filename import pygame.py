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