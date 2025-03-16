import pygame
import random

class Cactus(pygame.sprite.Sprite):
    def __init__(self, frames, x, y, speed):
        super().__init__()
        self.image = random.choice(frames)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.bottom = y
        self.speed = speed

    def update(self):
        self.rect.x -= self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def offscreen(self):
        return self.rect.right < 0
