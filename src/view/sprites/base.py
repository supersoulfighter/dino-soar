from typing import Sequence
import pygame
import random



class SpriteBase(pygame.sprite.Sprite):
    def __init__(self, images, x, y, useMask=False, *groups, **kwargs):
        super().__init__(*groups)
        self.useMask = useMask
        if isinstance(images, Sequence):
            self.image = random.choice(images)
        elif isinstance(images, pygame.Surface):
            self.image = images
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.bottom = y


    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value
        if self.useMask:
            self.mask = pygame.mask.from_surface(self.image)
        # All animation frames should have the same size, so rect not updated
 