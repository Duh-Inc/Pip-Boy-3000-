import pygame
import config
import datetime

class Header:
    def __init__(self, mainTab, playerData):
        self.mainTab = mainTab
        self.playerData = playerData
        self.cornerPadding = 10
        self.canvasHeight = 60
        self.canvas = pygame.Surface((config.WIDTH, self.canvasHeight))
        self.canvas.fill(config.BG_COLOR)

        self.infoMap = {
            "Stats": ["LVL", "HP", "AP", "XP"],
            "Items": ["Wg", "HP", "DR", "Caps"],
            "Data": ["Location", "Date"],
        }

    def drawHeader(self):
        self.canvas.fill(config.BG_COLOR)

        # Main tab text
        titleY = 8
        titleImg = config.FONT_LRG.render(self.mainTab.upper(), True, config.DRAWCOLOUR)
        titleX = self.cornerPadding + 35  # shifted further right
        self.canvas.blit(titleImg, (titleX, titleY))

        # Horizontal line with gap for main tab
        lineY = titleY + titleImg.get_height() // 2
        gap = 6
        titleWidth = titleImg.get_width()

        pygame.draw.line(
            self.canvas,
            config.DRAWCOLOUR,
            (self.cornerPadding, lineY),
            (titleX - gap, lineY),
            2,
        )
        pygame.draw.line(
            self.canvas,
            config.DRAWCOLOUR,
            (titleX + titleWidth + gap, lineY),
            (config.WIDTH - self.cornerPadding, lineY),
            2,
        )

        # Vertical end lines (thicker)
        verticalThickness = 2
        pygame.draw.line(self.canvas, config.DRAWCOLOUR,
                         (self.cornerPadding, lineY),
                         (self.cornerPadding, self.canvasHeight - self.cornerPadding),
                         verticalThickness)
        pygame.draw.line(self.canvas, config.DRAWCOLOUR,
                         (config.WIDTH - self.cornerPadding, lineY),
                         (config.WIDTH - self.cornerPadding, self.canvasHeight - self.cornerPadding),
                         verticalThickness)

        # Right-aligned data points with L-shaped separators
        infoKeys = self.infoMap.get(self.mainTab, [])
        if infoKeys:
            infoX = config.WIDTH - self.cornerPadding - 10  # spacing from end
            infoY = lineY + 2
            spacing = 12

            for i in reversed(range(len(infoKeys))):
                key = infoKeys[i]
                if key == "Date":
                    now = datetime.datetime.now()
                    val = now.strftime("%m.%d.%y %H:%M")
                else:
                    val = self.playerData.get(key, "--")

                text = f"{key} {val}"
                textImg = config.FONT_SM.render(text, True, config.DRAWCOLOUR)
                infoX -= textImg.get_width()
                self.canvas.blit(textImg, (infoX, infoY))

                # Vertical L-line separator (skip last one)
                if i != 0:
                    sepX = infoX - spacing
                    pygame.draw.line(
                        self.canvas,
                        config.DRAWCOLOUR,
                        (sepX, lineY),
                        (sepX, infoY + textImg.get_height()),
                        verticalThickness,
                    )
                    infoX = sepX - spacing

        return self.canvas


class Footer:
    def __init__(self, mainTab, currentSubtab):
        self.mainTab = mainTab
        self.currentSubtab = currentSubtab
        self.cornerPadding = 10
        self.canvasHeight = 60
        self.canvas = pygame.Surface((config.WIDTH, self.canvasHeight))
        self.canvas.fill(config.BG_COLOR)

        self.subtabs = {
            "Stats": ["Status", "S.P.E.C.I.A.L.", "Skills", "Perks", "General"],
            "Items": ["Weapons", "Apparel", "Aid", "Misc", "Ammo"],
            "Data": ["Local Map", "World Map", "Quests", "Misc", "Radio"],
        }[mainTab]

    def drawFooter(self):
        self.canvas.fill(config.BG_COLOR)

        TextXPadding = config.charHeight
        TextCentreDiff = (config.WIDTH - (TextXPadding * 2)) / 5
        TextCentreX = TextXPadding + (TextCentreDiff / 2)
        TextY = self.canvasHeight - config.charHeight - 2

        # Horizontal line
        btmPad = self.canvasHeight - self.cornerPadding
        rgtPad = config.WIDTH - self.cornerPadding
        lineUp = btmPad - (config.charHeight * 1.6)
        verticalThickness = 2
        pygame.draw.lines(
            self.canvas,
            config.DRAWCOLOUR,
            False,
            [
                (self.cornerPadding, lineUp),
                (self.cornerPadding, btmPad),
                (rgtPad, btmPad),
                (rgtPad, lineUp),
            ],
            verticalThickness,
        )

        # Draw 5 subtabs
        for i, stName in enumerate(self.subtabs):
            isActive = (i + 1) == self.currentSubtab
            BoxGrey = config.SELBOXGREY if isActive else 0
            BoxColour = (BoxGrey, BoxGrey, BoxGrey)

            textImg = config.FONT_SM.render(stName, True, config.DRAWCOLOUR, BoxColour)

            TextWidth = textImg.get_width()
            TextX = TextCentreX - (TextWidth / 2)
            textPos = (TextX, TextY)

            # Background box
            TextRect = (TextX - 2, TextY - 2, TextWidth + 4, config.charHeight + 4)
            pygame.draw.rect(self.canvas, BoxColour, TextRect, 0)

            # Highlight border if selected
            if isActive:
                selRect = (TextRect[0] - 2, TextRect[1], TextRect[2] + 2, TextRect[3])
                pygame.draw.rect(self.canvas, config.DRAWCOLOUR, selRect, 2)

            self.canvas.blit(textImg, textPos)
            TextCentreX += TextCentreDiff

        return self.canvas
