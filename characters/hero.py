#!/usr/bin/env python3

from characters.base import Character

class Hero(Character):

    # all movements don't allow the hero to exit the screen
    def move_up(self):
        if self.y - self.increment < 0 :
            self.y = 0
        else:
            self.y -= self.increment

    def move_down(self):
        if self.y + self.height + self.increment > self.bg_height:
            self.y = self.bg_height - self.height
        else:
            self.y += self.increment

    def move_right(self):
        if self.x + self.width + self.increment > self.bg_width:
            self.x = self.bg_width - self.width
        else:
            self.x += self.increment

    def move_left(self):
        if self.x - self.increment < 0:
            self.x = 0
        else:
            self.x -= self.increment
