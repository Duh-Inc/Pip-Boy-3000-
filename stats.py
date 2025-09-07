import pygame
import config

class Tab_Stats:

    name = "STATS"

    class Mode_Subtab:
        def __init__(self, parent, name="Subtab"):
            self.parent = parent
            self.name = name
            self.pageCanvas = pygame.Surface((config.WIDTH, config.HEIGHT))
            self.changed = True

        def drawPage(self):
            if not self.changed:
                return self.pageCanvas, False
            self.pageCanvas.fill((10, 10, 30))
            font = config.FONT_LRG
            img = font.render(self.name, True, config.DRAWCOLOUR)
            self.pageCanvas.blit(img, (50, 50))
            self.changed = False
            return self.pageCanvas, True

        def resetPage(self):
            self.changed = True

        def ctrlEvents(self, events):
            pass

    def __init__(self, parent):
        self.parent = parent
        self.modes = [self.Mode_Subtab(self, name) for name in ["Status", "S.P.E.C.I.A.L.", "Skills", "Perks", "General"]]
        self.name = self.name

    def drawPage(self, modeNum):
        return self.modes[modeNum].drawPage()

    def resetPage(self, modeNum):
        self.modes[modeNum].resetPage()

    def ctrlEvents(self, events, modeNum):
        self.modes[modeNum].ctrlEvents(events)
