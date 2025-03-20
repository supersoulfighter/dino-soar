from typing import override
import pygame



class Screen(pygame.sprite.LayeredUpdates):
    """
    Screen
    ======
    *This class creates and manages the game window and handles all rendering.
    By subclassing ``pygame.Group`` and adding all game objects
    (``Sprites`` and ``Groups``), we can update and render all game objects
    in one place.*

    Parameters
    ----------
        width: Width of the window
        height: Height of the window
        caption: Caption of the window
        color_bg: Background color
    """

    def __init__(self, width, height, caption, color_bg):
        super().__init__()
        self.image = pygame.display.set_mode((width, height))
        pygame.display.set_caption(caption)
        self.rect = self.image.get_rect()
        self.groups = []
        self.color_bg = color_bg


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