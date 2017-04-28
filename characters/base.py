#!/usr/bin/env python3

import get_png_dimensions
import os
import pygame
import math
import random

class Character:
    def __init__(self, filename = "", increment = 0, bg = (), screen = None):
        self.filename = filename
        self.increment = increment
        self.width, self.height = get_png_dimensions.png_info(os.path.join("images",self.filename))
        self.load = pygame.image.load(os.path.join("images", self.filename))
        self.bg_width, self.bg_height = bg
        self.screen = screen
        self.caught = False
        self.x = 0
        self.y = 0
        self.random_position()

    def catch(self, enemy):
        if math.sqrt(pow(self.x + self.width/2 - (enemy.x + enemy.width/2), 2) + pow(self.y + self.height/2 - (enemy.y + enemy.height/2), 2)) < 32:
            self.caught = True
            return True

    def display(self):
        return self.screen.blit(self.load, (self.x, self.y))

    def random_position(self):
        self.x = random.randint(0, self.bg_width-self.width)
        self.y = random.randint(0, self.bg_height-self.height)
