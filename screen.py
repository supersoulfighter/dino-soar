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
        self.image.fill(COLOR_BACKGROUND)
        super().draw(self.image)
        display.flip()