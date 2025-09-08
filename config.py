# config.py
import pygame
import os

# ----------------- SCREEN -----------------
WIDTH = 480      # your Pi screen width
HEIGHT = 320     # your Pi screen height
BG_COLOR = (0, 0, 0)
FG_COLOR = (0, 255, 0)       # green text like Pip-Boy
DRAWCOLOUR = (0, 255, 0)
SELBOXGREY = 50               # gray for selected box

# ----------------- FONT -------------------
# Path to your Monofonto OTF
FONT_PATH = os.path.join(os.path.dirname(__file__), "Monofonto.otf")

# Character height (approx)
CHAR_HEIGHT = 16
charHeight = CHAR_HEIGHT  # for headFoot compatibility

# Initialize pygame font system
pygame.font.init()
FONT_SM = pygame.font.Font(FONT_PATH, 14)  # small font for subtabs
FONT_LRG = pygame.font.Font(FONT_PATH, 18)  # large font for headers, modes

# ----------------- OTHER -----------------
MUSIC_FOLDER = os.path.join(os.path.dirname(__file__), "music")
DEFAULT_COVER = pygame.Surface((100, 100))
DEFAULT_COVER.fill((0, 255, 0))
