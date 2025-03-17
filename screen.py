from typing import override
from config import *
from pygame import display


class Screen(pygame.sprite.LayeredUpdates):
    def __init__(self, width, height, caption):
        super().__init__()
        self.image = display.set_mode((width, height))
        display.set_caption(caption)
        self.rect = self.image.get_rect()
        self.groups = []

    @override
    def add(self, *sprites, **kwargs):
        if len(sprites) > 0 and isinstance(sprites[0], pygame.sprite.Group):
            self.groups.append(sprites[0])
        super().add(*sprites, **kwargs)

    @override
    def empty(self, *args, **kwargs):
        self.groups.clear()
        super().empty(*args, **kwargs)

    @override
    def update(self, *args, **kwargs) -> None:
        for group in self.groups:
            group.update(*args, **kwargs)
        return super().update(*args, **kwargs)

    def render(self):
        self.image.fill(COLOR_BACKGROUND)
        super().draw(self.image)
        display.flip()