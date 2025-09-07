# controls.py
import pygame

class Controls:
    """
    Stores the current input state.
    Scroll wheel = navigation
    Scroll button = select/play
    Keys S/I/D = switch tabs
    Keys 1-5 = switch subtabs
    """
    def __init__(self):
        self.scrollDelta = 0
        self.scrollButtonPressed = False
        self.tabKey = None
        self.subtabKey = None

    def update(self, events):
        # reset values each frame
        self.scrollDelta = 0
        self.scrollButtonPressed = False
        self.tabKey = None
        self.subtabKey = None

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:  # scroll up
                    self.scrollDelta = 1
                elif event.button == 5:  # scroll down
                    self.scrollDelta = -1
                elif event.button == 2:  # middle-click / scroll button
                    self.scrollButtonPressed = True

            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_s, pygame.K_i, pygame.K_d):
                    self.tabKey = event.key
                elif event.key in (pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5):
                    self.subtabKey = int(event.unicode)
