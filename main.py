import pygame
import os
from controls import Controls
from io import BytesIO
from mutagen.id3 import ID3, error
import random

# ------------------- CONFIG -------------------
WIDTH, HEIGHT = 480, 320
BG_COLOR = (0, 0, 0)
FG_COLOR = (0, 255, 0)
FONT_SM = pygame.font.SysFont("Consolas", 16)
FONT_LRG = pygame.font.SysFont("Consolas", 20)

# Example data for stats/items
STATS = {
    "Status": ["HP: 100/100", "AP: 50/50", "Radiation: 0"],
    "S.P.E.C.I.A.L.": ["S:5", "P:6", "E:5", "C:7", "I:6", "A:4", "L:3"],
    "Skills": ["Lockpicking: 50%", "Science: 60%", "Sneak: 40%"],
    "Perks": ["Nerd Rage", "Gun Nut", "Strong Back"],
    "General": ["Level: 10", "XP: 5400/6000"]
}

ITEMS = {
    "Weapons": ["10mm Pistol", "Laser Rifle", "Combat Knife"],
    "Apparel": ["Leather Armor", "Vault Suit", "Power Armor Helmet"],
    "Aid": ["Stimpak", "RadAway", "Med-X"],
    "Misc": ["Bottle Caps", "Holotape", "Fusion Core"],
    "Ammo": ["10mm Rounds", "Energy Cells", "Shotgun Shells"]
}

DATA = {
    "Local Map": None,  # Placeholder
    "World Map": None,  # Placeholder
    "Quests": ["Find Dogmeat", "Clear Sanctuary", "Deliver Pip-Boy"],
    "Misc": ["Holotape", "Bottle Caps", "Stimpaks"],
    "Radio": []  # Populated from 'music' folder
}

MUSIC_FOLDER = "music"
DEFAULT_COVER = pygame.Surface((100, 100))
DEFAULT_COVER.fill((30, 30, 30))


# ------------------- RADIO -------------------
class Radio:
    def __init__(self):
        self.tracks = self.loadTracks()
        self.index = 0
        self.cover = DEFAULT_COVER
        self.title = ""
        self.playing = False
        try:
            pygame.mixer.init()
        except pygame.error:
            print("Audio not initialized")
        self.updateMetadata()

    def loadTracks(self):
        if not os.path.isdir(MUSIC_FOLDER):
            os.makedirs(MUSIC_FOLDER)
        tracks = [os.path.join(MUSIC_FOLDER, f) for f in os.listdir(MUSIC_FOLDER) if f.lower().endswith(".mp3")]
        return sorted(tracks)

    def updateMetadata(self):
        if not self.tracks:
            self.title = "No tracks"
            self.cover = DEFAULT_COVER
            return
        fp = self.tracks[self.index]
        try:
            tags = ID3(fp)
            self.title = tags.get("TIT2", os.path.basename(fp)).text[0] if "TIT2" in tags else os.path.basename(fp)
        except error:
            self.title = os.path.basename(fp)
        self.cover = DEFAULT_COVER

    def nextTrack(self):
        if self.tracks:
            self.index = (self.index + 1) % len(self.tracks)
            self.updateMetadata()
            self.play()

    def prevTrack(self):
        if self.tracks:
            self.index = (self.index - 1) % len(self.tracks)
            self.updateMetadata()
            self.play()

    def play(self):
        if pygame.mixer.get_init() and self.tracks:
            try:
                pygame.mixer.music.load(self.tracks[self.index])
                pygame.mixer.music.play()
                self.playing = True
            except pygame.error:
                self.playing = False

    def togglePlay(self):
        if pygame.mixer.get_init() and self.tracks:
            if self.playing and pygame.mixer.music.get_busy():
                pygame.mixer.music.pause()
                self.playing = False
            elif self.tracks:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.unpause()
                else:
                    self.play()
                self.playing = True


# ------------------- INITIALIZATION -------------------
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pip-Boy Emulator")
clock = pygame.time.Clock()

controls = Controls()
currentTab = "Stats"
currentSubtab = 1
radio = Radio()

running = True

# Scroll positions for lists
scrolls = {}

def getList(tab, subtab):
    if tab == "Stats":
        return STATS.get(subtab, [])
    elif tab == "Items":
        return ITEMS.get(subtab, [])
    elif tab == "Data":
        if subtab in ["Quests", "Misc"]:
            return DATA[subtab]
        return []


# ------------------- MAIN LOOP -------------------
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    controls.update(events)

    # Tab switching
    if controls.tabKey:
        if controls.tabKey == pygame.K_s:
            currentTab = "Stats"
        elif controls.tabKey == pygame.K_i:
            currentTab = "Items"
        elif controls.tabKey == pygame.K_d:
            currentTab = "Data"
        currentSubtab = 1

    # Subtab switching
    if controls.subtabKey:
        currentSubtab = controls.subtabKey

    # Scrollable content
    key = (currentTab, currentSubtab)
    if key not in scrolls:
        scrolls[key] = 0
    lst = getList(currentTab, list(SUBTABS := {
        "Stats": ["Status", "S.P.E.C.I.A.L.", "Skills", "Perks", "General"],
        "Items": ["Weapons", "Apparel", "Aid", "Misc", "Ammo"],
        "Data": ["Local Map", "World Map", "Quests", "Misc", "Radio"]
    }[currentTab])[currentSubtab - 1])
    if controls.scrollDelta != 0:
        scrolls[key] = max(0, min(len(lst) - 5, scrolls[key] - controls.scrollDelta))

    # Radio controls
    if currentTab == "Data" and list(SUBTABS["Data"])[currentSubtab - 1] == "Radio":
        if controls.scrollDelta > 0:
            radio.nextTrack()
        elif controls.scrollDelta < 0:
            radio.prevTrack()
        if controls.scrollButtonPressed:
            radio.togglePlay()

    # ------------------- DRAW -------------------
    screen.fill(BG_COLOR)

    # Draw tabs
    for i, t in enumerate(["Stats", "Items", "Data"]):
        color = FG_COLOR if t == currentTab else (100, 100, 100)
        txt = FONT_LRG.render(t, True, color)
        screen.blit(txt, (10 + i * 150, 10))

    # Draw subtabs
    for i, st in enumerate(SUBTABS[currentTab]):
        color = FG_COLOR if (i + 1) == currentSubtab else (100, 100, 100)
        txt = FONT_SM.render(st, True, color)
        screen.blit(txt, (10 + i * 90, 50))

    # Draw content area
    contentY = 90
    if currentTab in ["Stats", "Items"]:
        visible = lst[scrolls[key]:scrolls[key] + 5]
        for i, item in enumerate(visible):
            txt = FONT_SM.render(item, True, FG_COLOR)
            screen.blit(txt, (20, contentY + i * 20))
    elif currentTab == "Data":
        st_name = SUBTABS["Data"][currentSubtab - 1]
        if st_name in ["Local Map", "World Map"]:
            # Placeholder map
            pygame.draw.rect(screen, (50, 50, 100), (20, contentY, 440, 200))
            # Random "player location" dot
            pygame.draw.circle(screen, (255, 0, 0), (random.randint(50, 430), random.randint(50, 180)), 5)
        elif st_name in ["Quests", "Misc"]:
            visible = lst[scrolls[key]:scrolls[key] + 5]
            for i, item in enumerate(visible):
                txt = FONT_SM.render(item, True, FG_COLOR)
                screen.blit(txt, (20, contentY + i * 20))
        elif st_name == "Radio":
            screen.blit(radio.cover, radio.cover.get_rect(center=(WIDTH//2, contentY + 50)))
            title_txt = FONT_SM.render(radio.title, True, FG_COLOR)
            screen.blit(title_txt, (WIDTH//2 - title_txt.get_width()//2, contentY + 160))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
