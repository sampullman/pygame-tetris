import os

main_dir = os.path.split(os.path.abspath(__file__))[0]  # Program's diretory

FPS = 25
INITIAL_SPEED = 1000
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 600
WORLD_WIDTH = 22
WORLD_HEIGHT = 24
CELL_WIDTH = SCREEN_WIDTH / WORLD_WIDTH
CELL_HEIGHT = SCREEN_HEIGHT / WORLD_HEIGHT
BOARD_WIDTH = 10
BOARD_HEIGHT = 20
BG_COLOR = (240, 240, 240)

# Block array indices
RED=1
YELLOW=2
PURPLE=3
GREEN=4
BLUE=5
ORANGE=6
CYAN=7

# Movement directions
LEFT=0
RIGHT=1
DOWN=2
ROT_LEFT=3
ROT_RIGHT=4
