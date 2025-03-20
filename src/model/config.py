"""
Game Configuration
==================
*Constants that configure the game*

Most modules in this project have this module as an import dependency, which is not necessarily good practice. The alternative, furnishing all configuration data at the time of object construction, was judged to be unnecessary overhead for a young coder. The resulting code looks a little less imposing and requires less typing.
"""
from enum import Enum, auto
import pygame



#Game constants first because some are used by other constants
GAME_FPS = 60
GAME_WIDTH = 600
GAME_HEIGHT = 150
GAME_NAME = "Dino Soar"
GAME_SPEED_INCREMENT = .001
GAME_SPEED_MAX = 1000
GAME_SPEED_START = 6

GROUND_Y = GAME_HEIGHT - 15

CACTI_CLUSTER_MAX = 4
CACTI_WIDTH_MAX = 75
CACTI_SPACING_MIN = -12
CACTI_SPACING_MAX = 4

OBSTACLE_SPAWN_VARIANCE = 50
OBSTACLE_SPAWN_RATE = 130

PTERODACTYL_ANIMATION_SPEED = .06
PTERODACTYL_SPEED_MULTIPLIER = 1.1
PTERODACTYL_SPAWN_AT_SCORE= 1000
PTERODACTYL_SPAWN_PROBABILITY = .33
PTERODACTYL_MIN_Y = 50
PTERODACTYL_MAX_Y = 123

CLOUD_MAX_Y = GAME_HEIGHT - 30
CLOUD_MIN_Y = 10
CLOUD_SPAWN_CHANCE = .004
CLOUD_SPEED_MULTIPLIER = .2

COLOR_BACKGROUND = (255, 255, 255)
COLOR_FOREGROUND = (83, 83, 83)

DINO_ANIMATION_SPEED = 0.25
DINO_GRAVITY = .7
DINO_JUMP_SPEED = -10.5
DINO_START_X = 0
DINO_START_Y = GROUND_Y

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

