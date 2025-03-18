import pygame
from model.assets import assets
from view.sprites.base import SpriteBase



class SpriteAnimating(SpriteBase):
    def __init__(self, images, animation_speed, state_start, x, y, useMask=False, *groups, **kwargs):
        self.useMask = useMask
        self.animations = images
        self.animation_speed = animation_speed
        self._state = None
        self.state = state_start
        self.animate()
        super().__init__(images=images, x=x, y=y, useMask=useMask, *groups, **kwargs)



    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        if value == self._state:
            return
        self.state_previous = self._state
        self._state = value
        self.animation_time = 0
        self.animation_frame = 0
        self.animation_length = 0 if isinstance(self.animations[value], pygame.Surface) else len(self.animations[value])


    def update(self):
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