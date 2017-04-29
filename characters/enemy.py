#!/usr/bin/env python3

from characters.base import Character
import random
import time

class Enemy(Character):
    def __init__(self, *args, time = 0, **kwargs):
        super().__init__(*args, **kwargs)
        self.time = time
        self.counter = 1

    # moves in the random direction
    def move_random(self):
        if self.counter == self.time * 60:
            self.counter = 1
            return self.random_choice()
        else:
            self.counter += 1
            return self.display()

    # choses randomly a direction to move
    def random_choice(self):
        choice = random.choice(["up", "down", "left", "right", "rightup", "rightdown", "leftup", "leftdown"])
        if choice == "up":
            return self.move_up()
        elif choice == "down":
            return self.move_down()
        elif choice == "left":
            return self.move_left()
        elif choice == "right":
            return self.move_right()
        elif choice == "rightup":
            return self.move_rightup()
        elif choice == "rightdown":
            return self.move_rightdown()
        elif choice == "leftup":
            return self.move_leftup()
        elif choice == "leftdown":
            return self.move_leftdown()

    # all movements allow to exit screen and enter from the opposite side
    def move_rightup(self):
        if self.y - self.increment + self.height < 0 :
            self.y = self.bg_height + self.y - self.increment
        elif self.x + self.increment > self.bg_width:
            self.x = 0 + self.increment - (self.bg_width-self.x)
        else:
            self.y -= self.increment
            self.x += self.increment

    def move_leftup(self):
        if self.y - self.increment + self.height < 0 :
            self.y = self.bg_height + self.y - self.increment
        elif self.x - self.increment + self.width < 0:
            self.x = self.bg_width + self.x - self.increment
        else:
            self.y -= self.increment
            self.x -= self.increment

    def move_rightdown(self):
        if self.y + self.increment > self.bg_height:
            self.y = 0 + self.increment - (self.bg_height-self.y)
        elif self.x + self.increment > self.bg_width:
            self.x = 0 + self.increment - (self.bg_width-self.x)
        else:
            self.y += self.increment
            self.x += self.increment

    def move_leftdown(self):
        if self.y + self.increment > self.bg_height:
            self.y = 0 + self.increment - (self.bg_height-self.y)
        elif self.x - self.increment + self.width < 0:
            self.x = self.bg_width + self.x - self.increment
        else:
            self.y += self.increment
            self.x -= self.increment

    def move_up(self):
        if self.y - self.increment + self.height < 0 :
            self.y = self.bg_height + self.y - self.increment
        else:
            self.y -= self.increment

    def move_down(self):
        if self.y + self.increment > self.bg_height:
            self.y = 0 + self.increment - (self.bg_height-self.y)
        else:
            self.y += self.increment

    def move_right(self):
        if self.x + self.increment > self.bg_width:
            self.x = 0 + self.increment - (self.bg_width-self.x)
        else:
            self.x += self.increment

    def move_left(self):
        if self.x - self.increment + self.width < 0:
            self.x = self.bg_width + self.x - self.increment
        else:
            self.x -= self.increment
