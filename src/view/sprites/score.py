from math import floor
import pygame
import model.assets
import model.game


class Score(pygame.sprite.Sprite):
    """
    Score
    =====
    *A sprite that displays the current score.*

    Parameters
    ----------
        ``x`` (int): The x-coordinate of the sprite.
        ``y`` (int): The y-coordinate of the sprite.
        ``color`` (tuple): The color of the sprite.
        ``font`` (pygame.Font, optional): The font to use for the sprite.
        Defaults to None.
    """
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
            model.assets.assets["sounds/score"].play()
