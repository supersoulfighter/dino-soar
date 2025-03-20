from typing import override
import pygame
from model.config import *

class Screen(pygame.sprite.LayeredUpdates):
    """
    Screen
    ======
    *This class creates and manages the game window and handles all rendering.*

    By subclassing ``pygame.Group`` and adding all game objects (``Sprites`` and ``Groups``), we can update and render all game objects in one place.
    """

    def __init__(self):
        super().__init__()
        self.image = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
        pygame.display.set_caption(GAME_NAME)
        self.rect = self.image.get_rect()
        self.groups = []
        self.color_bg = COLOR_BACKGROUND


    @override
    def add(self, *sprites, **kwargs):
        if len(sprites) > 0 and isinstance(sprites[0], pygame.sprite.Group):
            self.groups.append(sprites[0])
        super().add(*sprites, **kwargs)


    @override
    def remove(self, *sprites):
        if len(sprites) > 0:
            if isinstance(sprites[0], pygame.sprite.Group):
                if sprites[0] in self.groups:
                    self.groups.remove(sprites[0])
            super().remove(*sprites)


    @override
    def empty(self):
        self.groups.clear()
        super().empty()


    @override
    def update(self, *args, **kwargs) -> None:
        for group in self.groups:
            group.update(*args, **kwargs)
        return super().update(*args, **kwargs)


    def render(self):
        self.image.fill(self.color_bg)
        super().draw(self.image)
        pygame.display.flip()