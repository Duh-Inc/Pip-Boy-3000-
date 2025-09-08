import pygame
import sys
import config
import headFoot as hf
import datetime
from scanlines import ScanlineOverlay   # 👈 import the overlay

pygame.init()

# ----------------- TABS -----------------
MAIN_TABS = ["Stats", "Items", "Data"]
SUBTABS = {
    "Stats": ["Status", "S.P.E.C.I.A.L.", "Skills", "Perks", "General"],
    "Items": ["Weapons", "Apparel", "Aid", "Misc", "Ammo"],
    "Data": ["Local Map", "World Map", "Quests", "Misc", "Radio"]
}

# ----------------- STATE -----------------
currentTab = "Stats"       # Main tab
currentSubtab = 1          # Subtab index (1–5)

# ----------------- PLAYER DATA -----------------
playerData = {
    "LVL": 10,
    "HP": "100/100",
    "AP": "50/50",
    "XP": "5400/6000",
    "Wg": "7.62",
    "DR": "12",
    "Caps": 120,
    "Location": "Sanctuary",
}

# ----------------- PYGAME SETUP -----------------
screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
pygame.display.set_caption("Pip-Boy 3000")

clock = pygame.time.Clock()

# ----------------- OVERLAYS -----------------
scanlines = ScanlineOverlay(config.WIDTH, config.HEIGHT)   # 👈 init overlay

# ----------------- RENDER FUNCTIONS -----------------
def drawContent(tab, subtabIndex):
    """Draw the main content area (placeholder for now)."""
    subtab = SUBTABS[tab][subtabIndex - 1]
    text = f"{tab} → {subtab}"
    content = config.FONT_LRG.render(text, True, config.FG_COLOR)
    screen.blit(content, (50, 100))


def redraw():
    screen.fill(config.BG_COLOR)

    # Header
    header = hf.Header(currentTab, playerData)
    screen.blit(header.drawHeader(), (0, 0))

    # Content
    drawContent(currentTab, currentSubtab)

    # Footer
    footer = hf.Footer(currentTab, currentSubtab)
    screen.blit(footer.drawFooter(), (0, config.HEIGHT - footer.canvas.get_height()))

    # Overlays (draw last so they sit on top of everything)
    scanlines.update()
    scanlines.draw(screen)

    pygame.display.flip()


# ----------------- MAIN LOOP -----------------
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            # Cycle through main tabs
            elif event.key == pygame.K_LEFT:
                idx = MAIN_TABS.index(currentTab)
                currentTab = MAIN_TABS[(idx - 1) % len(MAIN_TABS)]
                currentSubtab = 1

            elif event.key == pygame.K_RIGHT:
                idx = MAIN_TABS.index(currentTab)
                currentTab = MAIN_TABS[(idx + 1) % len(MAIN_TABS)]
                currentSubtab = 1

            # Cycle through subtabs
            elif event.key == pygame.K_UP:
                currentSubtab = (currentSubtab - 2) % 5 + 1
            elif event.key == pygame.K_DOWN:
                currentSubtab = currentSubtab % 5 + 1

    redraw()
    clock.tick(30)

pygame.quit()
sys.exit()
