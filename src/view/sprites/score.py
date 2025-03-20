from math import floor
import pygame
import model.assets
import model.game
from model.config import *

class Score(pygame.sprite.Sprite):
    """
    Score
    =====
    *A sprite that displays the current score.*

    Also plays a sound every 100 points.
    """
    def __init__(self):
        super().__init__()
        self.font = pygame.font.Font(model.assets.assets["fonts/PressStart2P/regular"], FONT_SIZE)
        self.image = None
        self.rect = None
        self.update()

    def update(self):
        self.image = self.font.render(f"{floor(model.game.game_score):05d}", False, COLOR_FOREGROUND)
        self.rect = self.image.get_rect(topleft=(SCORE_X, SCORE_Y))
        if floor(model.game.game_score) % 100 == 0 and floor(model.game.game_score) > 0:
            model.assets.assets["sounds/score"].play()
