#!/usr/bin/env python3

import get_png_dimensions
import os
import pygame
import math
import random

class Character:
    def __init__(self, filename = "", increment = 0, bg = (), screen = None):
        self.filename = filename    # name of the png file that contains the character
        self.increment = increment  # the amount of pixels that the character will move in each iteration
        self.width, self.height = get_png_dimensions.png_info(os.path.join("images",self.filename))
                                    # automatically gets the dimensions of the character's png file
        self.load = pygame.image.load(os.path.join("images", self.filename))    # load the file into pygame
        self.bg_width, self.bg_height = bg  # receives the width and height of the background
        self.screen = screen        # receives the screen variable created in pygame
        self.caught = False         # sets the attribute that checks if the character caught another to False
        self.x = 0                  # sets the character's x coordinate
        self.y = 0                  # sets the character's y coordinate
        self.random_position()      # sets the x and y coordinates to a random position

    # checks if the characters have intersected
    def catch(self, enemy):
        if math.sqrt(pow(self.x + self.width/2 - (enemy.x + enemy.width/2), 2) + pow(self.y + self.height/2 - (enemy.y + enemy.height/2), 2)) < 32:
            self.caught = True
            return True

    # displays on screen
    def display(self):
        return self.screen.blit(self.load, (self.x, self.y))

    # generates a random position within the screen limits
    def random_position(self):
        self.x = random.randint(0, self.bg_width-self.width)
        self.y = random.randint(0, self.bg_height-self.height)
