# config.py
# Configuration for RasPipBoy 3000 Emulator

import pygame
import os

# ----------------- Display -----------------
WIDTH = 480        # width of the Pip-Boy screen in pixels
HEIGHT = 320       # height of the Pip-Boy screen in pixels
FPS = 30           # frames per second

# ----------------- Colors -----------------
DRAWCOLOUR = (0, 255, 0)       # classic green Pip-Boy text
BACKGROUND = (0, 0, 0)         # black background

# ----------------- Fonts -----------------
pygame.init()

# Try Monofonto first; fallback to Courier New if unavailable
FONT_PATH = "fonts/Monofonto.ttf"  # place Monofonto TTF here if you have it

if os.path.exists(FONT_PATH):
    FONT_SM = pygame.font.Font(FONT_PATH, 14)
    FONT_MD = pygame.font.Font(FONT_PATH, 16)
    FONT_LRG = pygame.font.Font(FONT_PATH, 18)
else:
    FONT_SM = pygame.font.SysFont("Courier New", 14)
    FONT_MD = pygame.font.SysFont("Courier New", 16)
    FONT_LRG = pygame.font.SysFont("Courier New", 18)

# ----------------- Character height -----------------
charHeight = FONT_SM.get_linesize()  # used for scrolling lists

# ----------------- Paths -----------------
MUSIC_FOLDER = "music"
FONT_FOLDER = "fonts"
DATA_FOLDER = "data"

# ----------------- Modules (placeholders) -----------------
# These will be replaced by your actual hardware modules later
gpsModule = None
gammaModule = None
