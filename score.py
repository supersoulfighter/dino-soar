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

    def update(self):
        self.score += self.clock.get_time() * self.pointsPerMillisecond
        self.image = self.font.render(f"{floor(self.score):05d}", False, self.color)
        # self.image = pygame.Surface(text.get_size(), pygame.SRCALPHA)
        # self.image.fill((0,0,0,0))  # Transparent background
        # self.image.blit(text, (0, 0))

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))