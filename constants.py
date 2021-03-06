import os

main_dir = os.path.split(os.path.abspath(__file__))[0]  # Program's diretory

FPS = 25
INITIAL_SPEED = 400
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 600
WORLD_WIDTH = 22
WORLD_HEIGHT = 24
CELL_WIDTH = SCREEN_WIDTH / WORLD_WIDTH
CELL_HEIGHT = SCREEN_HEIGHT / WORLD_HEIGHT
BOARD_WIDTH = 10
BOARD_HEIGHT = 20
BOARD_OFFSET_X = 2
BOARD_OFFSET_Y = 2
PREVIEW_OFFSET_X = 14
PREVIEW_OFFSET_Y = 2
PREVIEW_WIDTH = 5
PREVIEW_HEIGHT = 5
EASY_BUTTON_OFFSET_Y = 20
EASY_BUTTON_OFFSET_X = BOARD_WIDTH+BOARD_OFFSET_X+1
HARD_BUTTON_OFFSET_X = EASY_BUTTON_OFFSET_X+4
ENDLESS_BUTTON_OFFSET_Y = 20
ENDLESS_BUTTON_OFFSET_X = BOARD_WIDTH+BOARD_OFFSET_X+1
LEVELS_BUTTON_OFFSET_X = ENDLESS_BUTTON_OFFSET_X+4
BG_COLOR = (240, 240, 240)
OUTLINE_COLOR = (180, 180, 190)
FONT_COLOR = (50, 50, 50)
SCORE_MUL = (40, 100, 300, 1200)
EASY = 0
HARD = 1
ENDLESS = 0
LEVELS = 1
NEW_LEVEL = 1

# Block array indices
RED=1
YELLOW=2
PURPLE=3
GREEN=4
BLUE=5
ORANGE=6
CYAN=7
GRAY=8

# Movement directions
LEFT=0
RIGHT=1
DOWN=2
UP=3
ROT_LEFT=4
ROT_RIGHT=5
