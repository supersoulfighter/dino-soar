"""
Dino Soar
=========
*A partial clone of the `Chrome no-network, dinosaur runner game <chrome://dino/>`_*

https://source.chromium.org/chromium/chromium/src/+/main:components/neterror/resources/dino_game/

The code uses a Model View Controller (MVC) architecture. This module acts as the controller.

Known gameplay differences from the original game:
- No splash / intro screen
- No night mode
- No easter eggs / collectables
- No high score tracker
- No restart button
- No slow mode
- Score formula slightly different
- Cacti grouping slightly different
- Obstacle spawning logic slightly different
- Jump trajectory for dino slightly different
- Higher max speed
- Sounds are recorded, not synthesized?
- Not implemented for mobile device or other window sizes

Author: Jeff Ettenhofer

"""
#https://intellij-support.jetbrains.com/hc/en-us/community/posts/360000424900/comments/6118549407762

import pygame
from model.config import *
import model.assets
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
view = Screen()
model.assets.load_assets("./assets")

# Create game objects
dino = Dino()
ground = Ground()
clouds = Clouds()
obstacles = Obstacles(dino)
score = Score()
message = Message()

# Add sprites to screen with layers
view.add(ground, layer=SCREEN_LAYERS.GROUND.value)
view.add(clouds, layer=SCREEN_LAYERS.GROUND.value)
view.add(dino, layer=SCREEN_LAYERS.DINO.value)
view.add(score, layer=SCREEN_LAYERS.UI.value)
view.add(message, layer=SCREEN_LAYERS.UI.value)


def reset_game():
    global dino, obstacles, score, message
    model.game.game_score = 0
    message.message = ""
    if dino.state_previous == None or dino.state_previous == DinoStates.DUCKING:
        dino.state = DinoStates.RUNNING
    else:
        dino.state = dino.state_previous
    view.remove(obstacles)
    obstacles.empty()
    view.add(obstacles, layer=SCREEN_LAYERS.OBSTACLES.value)
    model.game.game_state = GAME_STATES.PLAYING


def crashed():
    model.game.game_state = GAME_STATES.CRASHED
    model.assets.assets["sounds/dino/crash"].play()
    message.message = "G A M E  O V E R\nPress R to restart"
    dino.state = DinoStates.CRASHED
    dino.update()


def update():
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                model.game.game_state = GAME_STATES.QUIT

            case pygame.KEYDOWN:
                if (event.key == pygame.K_SPACE or event.key == pygame.K_UP) \
                    and model.game.game_state == GAME_STATES.PLAYING:
                    dino.jump()

                if event.key == pygame.K_DOWN and model.game.game_state == GAME_STATES.PLAYING:
                    dino.duck(True)

                if event.key == pygame.K_r and model.game.game_state == GAME_STATES.CRASHED:
                    reset_game()

            case pygame.KEYUP:
                if event.key == pygame.K_DOWN and model.game.game_state == GAME_STATES.PLAYING:
                    dino.duck(False)
       
            case GAME_EVENT_TYPES.CRASH.value:
                crashed()

            case GAME_EVENT_TYPES.SPAWNED.value:
                view.add(event.object, layer=event.layer)


# Start game
reset_game()


# Game loop
while model.game.game_state != GAME_STATES.QUIT:
   update()
   if model.game.game_state == GAME_STATES.PLAYING:
       model.game.update()
       view.update()
   view.render()

pygame.quit()