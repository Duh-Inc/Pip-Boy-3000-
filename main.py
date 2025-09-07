# main.py
import pygame
from controls import Controls

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 480, 320
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pip-Boy Emulator")

# Font and color config
FONT = pygame.font.SysFont("Consolas", 20)
BG_COLOR = (0, 0, 0)
FG_COLOR = (0, 255, 0)

# Example tab/subtab structure
TABS = ["Stats", "Items", "Data"]
SUBTABS = {
    "Stats": ["Status", "S.P.E.C.I.A.L.", "Skills", "Perks", "General"],
    "Items": ["Weapons", "Apparel", "Aid", "Misc", "Ammo"],
    "Data": ["Local Map", "World Map", "Quests", "Misc", "Radio"]
}

# Initial states
currentTab = "Stats"
currentSubtab = 1

controls = Controls()

running = True
clock = pygame.time.Clock()

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    # Update controls
    controls.update(events)

    # Handle tab switching
    if controls.tabKey:
        if controls.tabKey == pygame.K_s:
            currentTab = "Stats"
        elif controls.tabKey == pygame.K_i:
            currentTab = "Items"
        elif controls.tabKey == pygame.K_d:
            currentTab = "Data"
        currentSubtab = 1  # reset subtab when switching tab

    # Handle subtab switching
    if controls.subtabKey:
        currentSubtab = controls.subtabKey

    # Render UI
    screen.fill(BG_COLOR)

    # Draw main tabs
    for i, tab in enumerate(TABS):
        color = FG_COLOR if tab == currentTab else (100, 100, 100)
        tab_text = FONT.render(tab, True, color)
        screen.blit(tab_text, (10 + i * 150, 10))

    # Draw subtabs
    for i, subtab in enumerate(SUBTABS[currentTab]):
        color = FG_COLOR if (i + 1) == currentSubtab else (100, 100, 100)
        subtab_text = FONT.render(subtab, True, color)
        screen.blit(subtab_text, (10 + i * 90, 50))

    # Draw placeholder content area
    content_text = FONT.render(f"Content: {SUBTABS[currentTab][currentSubtab - 1]}", True, FG_COLOR)
    screen.blit(content_text, (10, 120))

    # Draw scroll info
    scroll_text = FONT.render(f"Scroll delta: {controls.scrollDelta}", True, FG_COLOR)
    screen.blit(scroll_text, (10, 160))

    scroll_button_text = FONT.render(f"Scroll button pressed: {controls.scrollButtonPressed}", True, FG_COLOR)
    screen.blit(scroll_button_text, (10, 180))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
