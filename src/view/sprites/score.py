from math import floor
import pygame
from model.assets import *
import model.game


class ScoreView(pygame.sprite.Sprite):
    def __init__(self, x, y, color, font=None):
        super().__init__()
        self.x = x
        self.y = y
        self.color = color
        self.font = font
        self.image = None
        self.rect = None
        self.update()

    def update(self):
        self.image = self.font.render(f"{floor(model.game.game_score):05d}", False, self.color)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        if floor(model.game.game_score) % 100 == 0 and floor(model.game.game_score) > 0:
            assets["sounds/score"].play()
