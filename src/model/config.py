# Game Configuration
from enum import Enum, auto
import pygame



#Game constants first because some are used by other constants
GAME_FPS = 60
GAME_HEIGHT = 150
GAME_NAME = "Dino Soar"
GAME_SPEED_INCREMENT = 1
GAME_SPEED_START = 5
GAME_WIDTH = 600
GAME_GROUND_Y = GAME_HEIGHT - 15

CLOUD_MAX_Y = GAME_HEIGHT - 30
CLOUD_MIN_Y = 10
CLOUD_SPAWN_CHANCE = .004
CLOUD_SPEED_MULTIPLIER = .3

COLOR_BACKGROUND = (255, 255, 255)
COLOR_FOREGROUND = (83, 83, 83)

DINO_ANIMATION_SPEED = 0.1
DINO_GRAVITY = .4
DINO_JUMP_SPEED = -8
DINO_START_X = 0
DINO_START_Y = GAME_GROUND_Y

FONT_SIZE = 13

MESSAGE_LINE_SPACING = 3
MESSAGE_X = GAME_WIDTH//2
MESSAGE_Y = GAME_HEIGHT//2 - 25

SCORE_POINTS_PER_MILLISECOND = 0.01
SCORE_X = GAME_WIDTH - 80
SCORE_Y = 10

class GAME_STATES(Enum):
    INTRO = auto()
    PLAYING = auto()
    CRASHED = auto()
    QUIT = auto()

class GAME_EVENT_TYPES(Enum):
    CRASH = pygame.event.custom_type()
    SPAWNED = pygame.event.custom_type()

class SCREEN_LAYERS(Enum):
    GROUND = auto()
    OBSTACLES = auto()
    DINO = auto()
    UI = auto()

