import pygame
from assets import *
from dino import *
from ground import *
from score import *
from message_on_screen import *
from obstacle_group import ObstacleGroup
from config import *



# Setup pygame, display and assets
pygame.init()
screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption("Dino Jump")
clock = pygame.time.Clock()
load_assets("./assets")


def reset_game():
    global dino, ground, obstacles, game_over, score, message_onscreen, game_active, scrolling_speed
    scrolling_speed = 5
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
    obstacles = ObstacleGroup(GAME_WIDTH,GROUND_Y, scrolling_speed)
    font = pygame.font.Font(assets["fonts/PressStart2P/regular"], 13)
    score = Score(GAME_WIDTH - 80, 10, COLOR_FOREGROUND, clock, 0.01, font)
    message_onscreen = MessageOnScreen(GAME_WIDTH//2, GAME_HEIGHT//2 - 25, 3, COLOR_FOREGROUND, font)
    game_over = False
    game_active = True


def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            global game_active
            game_active = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                dino.jump()
            if event.key == pygame.K_r and game_over:
                reset_game()


def update_game_objects():
    dino.update()
    ground.update()
    obstacles.update()
    score.update()
    message_onscreen.update()


def check_collisions():
    if obstacles.check_collision(dino):
        global game_over
        game_over = True
        assets["sounds/dino/crash"].play()
        message_onscreen.message = "G A M E  O V E R\nPress R to restart"
        message_onscreen.update()
        dino.state = DinoStates.CRASHED
        dino.update()

def render():
    screen.fill(COLOR_BACKGROUND)
    ground.draw(screen)
    dino.draw(screen)
    obstacles.draw(screen)
    score.draw(screen)
    message_onscreen.draw(screen)
    pygame.display.flip()



# Game loop
reset_game()
while game_active:
    handle_events()
    if not game_over:
        update_game_objects()
        check_collisions()
    render()
    clock.tick(FPS)

pygame.quit()