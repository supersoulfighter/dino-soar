# Game Configuration
from enum import Enum
import pygame

GAME_WIDTH = 600
GAME_HEIGHT = 150
GROUND_Y = GAME_HEIGHT - 15
FPS = 60
COLOR_BACKGROUND = (255, 255, 255)
COLOR_FOREGROUND = (83, 83, 83)

class GAME_EVENT_TYPES(Enum):
    CRASH = pygame.event.custom_type()
    SPAWNED = pygame.event.custom_type()

class SCREEN_LAYERS(Enum):
    GROUND = 0
    OBSTACLES = 1
    DINO = 2
    UI = 3

