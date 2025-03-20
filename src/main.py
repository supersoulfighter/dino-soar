"""
Dino Soar
=========
*A partial clone of the Chrome no-network, dinosaur runner game.*

Author: Jeff Ettenhofer
"""

import pygame
from model.config import *
from model.assets import *
import model.game
from view.sprites.dino import *
from view.sprites.score import *
from view.sprites.message import *
from view.groups.ground import *
from view.groups.obstacles import *
from view.groups.clouds import *
from view.screen import *

# Setup
pygame.init()
screen = Screen(GAME_WIDTH, GAME_HEIGHT, GAME_NAME, COLOR_BACKGROUND)
load_assets("../assets")

# Create game objects
dino = Dino(
    animations={
            DinoStates.RUNNING: assets["images/dino/run"],
            DinoStates.JUMPING: assets["images/dino/idle"],
            DinoStates.CRASHED: assets["images/dino/crash"]
        },
    animation_speed=DINO_ANIMATION_SPEED,
    state_start=DinoStates.RUNNING,
    x=DINO_START_X,
    y=DINO_START_Y,
    ground_y=GAME_GROUND_Y,
    useMask=True,
    jump_speed=DINO_JUMP_SPEED,
    gravity=DINO_GRAVITY
)
ground = Ground(GAME_GROUND_Y, assets["images/ground"])
clouds = Clouds(CLOUD_SPEED_MULTIPLIER, CLOUD_SPAWN_CHANCE, CLOUD_MIN_Y, CLOUD_MAX_Y)
obstacles = Obstacles(GAME_WIDTH, GAME_GROUND_Y, dino)
font = pygame.font.Font(assets["fonts/PressStart2P/regular"], FONT_SIZE)
score_view = ScoreView(SCORE_X, SCORE_Y, COLOR_FOREGROUND, font)
message_view = MessageView(MESSAGE_X, MESSAGE_Y, MESSAGE_LINE_SPACING, COLOR_FOREGROUND, font)

# Add sprites to screen with layers
screen.add(ground, layer=SCREEN_LAYERS.GROUND.value)
screen.add(clouds, layer=SCREEN_LAYERS.GROUND.value)
screen.add(dino, layer=SCREEN_LAYERS.DINO.value)
screen.add(score_view, layer=SCREEN_LAYERS.UI.value)
screen.add(message_view, layer=SCREEN_LAYERS.UI.value)


def reset_game():
    global dino, obstacles, score_view, message_view
    model.game.game_score = 0
    message_view.message = ""
    dino.state = dino.state_previous if dino.state_previous is not None else DinoStates.RUNNING
    screen.remove(obstacles)
    obstacles.empty()
    screen.add(obstacles, layer=SCREEN_LAYERS.OBSTACLES.value)
    model.game.game_state = GAME_STATES.PLAYING


def handle_events():
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                model.game.game_state = GAME_STATES.QUIT

            case pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and model.game.game_state == GAME_STATES.PLAYING:
                    dino.jump()
                if event.key == pygame.K_r and model.game.game_state == GAME_STATES.CRASHED:
                    reset_game()
       
            case GAME_EVENT_TYPES.CRASH.value:
                crashed()

            case GAME_EVENT_TYPES.SPAWNED.value:
                screen.add(event.object, layer=event.layer)


def crashed():
    model.game.game_state = GAME_STATES.CRASHED
    assets["sounds/dino/crash"].play()
    message_view.message = "G A M E  O V E R\nPress R to restart"
    dino.state = DinoStates.CRASHED
    dino.update()



# Game loop
reset_game()

while model.game.game_state != GAME_STATES.QUIT:
   handle_events()
   if model.game.game_state == GAME_STATES.PLAYING:
       model.game.update()
       screen.update()
   screen.render()

pygame.quit()