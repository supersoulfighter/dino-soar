import pygame
from enum import Enum, auto
from typing import override
from model.assets import *
from view.sprites.scrolling import SpriteScrolling
from view.sprites.animating import SpriteAnimating



class DinoStates(Enum):
    RUNNING = auto()
    JUMPING = auto()
    CRASHED = auto()



class Dino(SpriteAnimating):
    def __init__(self, animations, animation_speed, state_start, x, y, ground_y, useMask, jump_speed, gravity):
        super().__init__(images=animations, animation_speed=animation_speed, state_start=state_start, x=x, y=y, useMask=useMask)
        self.ground_y = ground_y
        self.jump_speed = jump_speed
        self.gravity = gravity
        self.velocity = 0


    def jump(self):
        if self.state == DinoStates.RUNNING:
            self.velocity = self.jump_speed
            self.state = DinoStates.JUMPING
            assets["sounds/dino/jump"].play()

    @override
    def update(self):
        self.animate()
        self.move()
    
    def move(self):
        if self.state == DinoStates.JUMPING:
            self.rect.y += self.velocity
            self.velocity += self.gravity
            if self.rect.bottom >= self.ground_y:
                self.rect.bottom = self.ground_y
                self.velocity = 0
                self.state = DinoStates.RUNNING