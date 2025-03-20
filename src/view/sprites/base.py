from typing import Sequence
import pygame
import random



class SpriteBase(pygame.sprite.Sprite):
    """
    SpriteBase
    ==========
    *Base sprite class.*
    
    The image and rect attributes enable any ``pygame.sprite.Group`` to draw the sprite.

    Parameters
    ----------
        ``images`` (Sequence or pygame.Surface): A ``Sequence`` of ``pygame.Surface`` objects or a single ``Surface``. If a ``Sequence`` is provided, a random one will be selected.
        ``x`` (int): The x-coordinate of the sprite.
        ``y`` (int): The y-coordinate of the sprite.
        ``useMask`` (bool, optional): Whether to create a collision mask for the sprite. Defaults to False.
        ``*groups`` (pygame.sprite.Group, optional): The ``Groups`` to add the sprite to.
    """
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
        # All images should have the same size, so rect not updated
