import pygame

class Controls:
    """Handle input emulation for Pip-Boy"""
    def __init__(self):
        self.tabKey = None
        self.subtabKey = None
        self.scrollDelta = 0
        self.scrollButtonPressed = False

    def update(self, events):
        self.tabKey = None
        self.subtabKey = None
        self.scrollDelta = 0
        self.scrollButtonPressed = False

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_s, pygame.K_i, pygame.K_d]:
                    self.tabKey = event.key
                elif event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5]:
                    self.subtabKey = int(event.unicode)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:  # scroll up
                    self.scrollDelta = 1
                elif event.button == 5:  # scroll down
                    self.scrollDelta = -1
                elif event.button == 2:  # middle-click
                    self.scrollButtonPressed = True
