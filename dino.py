import pygame
from enum import Enum, auto
from assets import assets


class DinoStates(Enum):
    RUNNING = auto()
    JUMPING = auto()
    CRASHED = auto()

class Dino(pygame.sprite.Sprite):
    def __init__(self, animations, animation_speed, state_start, x, y, ground_y, jump_speed, gravity):
        super().__init__()
        self.animations = animations
        self.animation_speed = animation_speed
        self.state = state_start
        self.animate()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.bottom = y
        self.ground_y = ground_y
        self.jump_speed = jump_speed
        self.gravity = gravity
        self.velocity = 0


    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
        self.animation_time = 0
        self.animation_frame = 0
        self.animation_length = 0 if isinstance(self.animations[value], pygame.Surface) else len(self.animations[value])

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value
        self.mask = pygame.mask.from_surface(self.image)
        

    def jump(self):
        if self.state == DinoStates.RUNNING:
            self.velocity = self.jump_speed
            self.state = DinoStates.JUMPING
            assets["sounds/dino/jump"].play()

    def move(self):
        if self.state == DinoStates.JUMPING:
            self.rect.y += self.velocity
            self.velocity += self.gravity
            if self.rect.bottom >= self.ground_y:
                self.rect.bottom = self.ground_y
                self.velocity = 0
                self.state = DinoStates.RUNNING

    def update(self):
        self.move()
        self.animate()
        
    def animate(self):
        if self.animation_length > 0:
            self.animation_time += self.animation_speed
            if self.animation_time >= self.animation_length:
                self.animation_time = 0
            self.animation_frame = int(self.animation_time)
            self.image = self.animations[self.state][self.animation_frame]
        else:
            self.image = self.animations[self.state]


