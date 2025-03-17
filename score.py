from math import floor
import pygame

class Score(pygame.sprite.Sprite):
    def __init__(self, x, y, color, clock, pointsPerMillisecond, font=None):
        super().__init__()
        self.x = x
        self.y = y
        self.color = color
        self.clock = clock
        self.pointsPerMillisecond = pointsPerMillisecond
        self.font = font
        self.score = 0
        self.image = None
        self.rect = None
        self.update()

    def update(self):
        self.score += self.clock.get_time() * self.pointsPerMillisecond
        self.image = self.font.render(f"{floor(self.score):05d}", False, self.color)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))