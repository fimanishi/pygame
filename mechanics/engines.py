#!/usr/bin/env python3

import pygame
import get_png_dimensions
import os
from characters.enemy import Enemy
from characters.hero import Hero

# compiles all the hero movements in one function
def hero_movement(hero):
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        hero.move_down()
    elif pygame.key.get_pressed()[pygame.K_UP]:
        hero.move_up()
    elif pygame.key.get_pressed()[pygame.K_LEFT]:
        hero.move_left()
    elif pygame.key.get_pressed()[pygame.K_RIGHT]:
        hero.move_right()

# set all enemies to move randomly
def enemy_movement(chars_dict):
    for i in chars_dict.keys():
        if i != "hero":
            chars_dict[i].move_random()

# displays all goblins
def goblins_display(chars_dict):
    for i in chars_dict.keys():
        if i != "hero" and i != "monster":
            chars_dict[i].display()

# identifies if a goblin caught the hero
def enemy_catch(chars_dict):
    for i in chars_dict.keys():
        if i != "hero" and i != "monster":
            if chars_dict[i].catch(chars_dict["hero"]) == True:
                return True

# set the characters in random positions
def chars_random_position(chars_dict):
    for i in chars_dict.values():
        i.random_position()

# creates a dictionary with all default characters
def create_chars_dict(bg_width, bg_height, screen):
    goblins = 3
    # creates a dictionary of the characters with the hero and the monster
    chars_dict = {"monster": Enemy("monster.png",  increment = 30, bg = (bg_width, bg_height), time = 0.3, screen = screen),
                  "hero": Hero("hero.png",  increment = 1, bg = (bg_width, bg_height), screen = screen)
                  }

    # creates the number of goblins desired and append to the characters' dictionary
    for goblin_count in range(1,goblins+1):
        key = "goblin" + str(goblin_count)
        chars_dict[key] = Enemy("goblin.png", increment = 10, bg = (bg_width, bg_height), time = 0.3, screen = screen)

    to_return = (chars_dict, goblin_count)
    return to_return
