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
screen = Screen(GAME_WIDTH, GAME_HEIGHT, GAME_NAME)
load_assets("./assets")


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
    ground_y=GROUND_Y,
    jump_speed=DINO_JUMP_SPEED,
    gravity=DINO_GRAVITY
)
ground = Ground(GROUND_Y, SCROLLING_SPEED_START, assets["images/ground"])
obstacles = Obstacles(GAME_WIDTH, GROUND_Y, SCROLLING_SPEED_START, dino)
font = pygame.font.Font(assets["fonts/PressStart2P/regular"], FONT_SIZE)
score = Score(SCORE_X, SCORE_Y, COLOR_FOREGROUND, clock, SCORE_POINTS_PER_MILLISECOND, font)
message_onscreen = MessageOnScreen(MESSAGE_X, MESSAGE_Y, MESSAGE_LINE_SPACING, COLOR_FOREGROUND, font)

# Add sprites to screen with layers
screen.add(ground, layer=SCREEN_LAYERS.GROUND.value)
# screen.add(obstacles, layer=SCREEN_LAYERS.OBSTACLES.value)
screen.add(dino, layer=SCREEN_LAYERS.DINO.value)
screen.add(score, layer=SCREEN_LAYERS.UI.value)
screen.add(message_onscreen, layer=SCREEN_LAYERS.UI.value)



def reset_game():
    global dino, obstacles, game_over, score, message_onscreen, game_active
    score.score = 0
    message_onscreen.message = ""
    dino.state = DinoStates.RUNNING
    screen.remove(obstacles)
    obstacles.empty()
    screen.add(obstacles, layer=SCREEN_LAYERS.OBSTACLES.value)
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