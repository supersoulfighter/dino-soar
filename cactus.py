import pygame
import random

class Cactus(pygame.sprite.Sprite):
    def __init__(self, images, x, y, speed):
        super().__init__()
        self.image = random.choice(images)
        self.rect.x = x
        self.rect.bottom = y
        self.speed = speed

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value
        self.rect = self._image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()  # Remove from all groups