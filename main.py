import pygame
from assets import *
from dino import *
from ground import *
from score import *
from message_on_screen import *
from obstacles import *
from config import *
from screen import Screen

# Setup
pygame.init()
clock = pygame.time.Clock()
screen = Screen(GAME_WIDTH, GAME_HEIGHT, "Dino Soar")
load_assets("./assets")


def reset_game():
    global dino, ground, obstacles, game_over, score, message_onscreen, game_active, scrolling_speed
    screen.empty()
    scrolling_speed = 5

    # Create game objects
    dino = Dino(
        animations={
                DinoStates.RUNNING: assets["images/dino/run"],
                DinoStates.JUMPING: assets["images/dino/idle"],
                DinoStates.CRASHED: assets["images/dino/crash"]
            },
        animation_speed=0.1,
        state_start=DinoStates.RUNNING,
        x=0,
        y=GROUND_Y,
        ground_y=GROUND_Y,
        jump_speed=-8,
        gravity=.4
    )
    ground = Ground(GROUND_Y, scrolling_speed, assets["images/ground"])
    obstacles = Obstacles(GAME_WIDTH, GROUND_Y, scrolling_speed, dino)
    font = pygame.font.Font(assets["fonts/PressStart2P/regular"], 13)
    score = Score(GAME_WIDTH - 80, 10, COLOR_FOREGROUND, clock, 0.01, font)
    message_onscreen = MessageOnScreen(GAME_WIDTH//2, GAME_HEIGHT//2 - 25, 3, COLOR_FOREGROUND, font)
    
    # Add sprites to screen with layers
    screen.add(ground, layer=SCREEN_LAYERS.GROUND.value)
    screen.add(obstacles, layer=SCREEN_LAYERS.OBSTACLES.value)
    screen.add(dino, layer=SCREEN_LAYERS.DINO.value)
    screen.add(score, layer=SCREEN_LAYERS.UI.value)
    screen.add(message_onscreen, layer=SCREEN_LAYERS.UI.value)
    
    game_over = False
    game_active = True


def handle_events():
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                global game_active
                game_active = False

            case pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not game_over:
                    dino.jump()
                if event.key == pygame.K_r and game_over:
                    reset_game()
       
            case GAME_EVENT_TYPES.CRASH.value:
                end_game()

            case GAME_EVENT_TYPES.SPAWNED.value:
                screen.add(event.object, layer=event.layer)


def end_game():
    global game_over
    game_over = True
    assets["sounds/dino/crash"].play()
    message_onscreen.message = "G A M E  O V E R\nPress R to restart"
    message_onscreen.update()
    dino.state = DinoStates.CRASHED
    dino.update()



# Game loop
reset_game()

while game_active:
    handle_events()
    if not game_over:
        screen.update()
    screen.render()
    clock.tick(FPS)

pygame.quit()