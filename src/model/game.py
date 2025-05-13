"""
Game
====
*Stores the game state:*

Make sure to use ``import model.game`` so that the specific global variables in this module are used, not copies.

* ``game_score``: The current score
* ``game_speed``: The current game speed
* ``game_state``: The current game state
* ``game_clock``: The game clock
"""
import pygame
from model.config import *

game_score = 0
game_speed = GAME_SPEED_START
game_state = GAME_STATES.INTRO
game_clock = pygame.time.Clock()

def update():
    """
    Update
    ======
    *Updates the game speed and score.*

    Should be called every frame.
    """
    global game_speed, game_score, game_clock
    if game_speed < GAME_SPEED_MAX:
        game_speed += GAME_SPEED_INCREMENT
    game_score += game_clock.get_time() * SCORE_POINTS_PER_MILLISECOND
    game_clock.tick(GAME_FPS)
