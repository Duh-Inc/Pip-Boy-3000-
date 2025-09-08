import pygame

class ScanlineOverlay:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.lastSweep = 0
        self.sweepDuration = 2000   # ms
        self.sweepInterval = 3000   # ms
        self.sweeping = False
        self.startTime = 0

        # Pre-render faint static scanlines (~10% opacity)
        self.scanlineBase = pygame.Surface((width, height), pygame.SRCALPHA)
        faint_alpha = int(255 * 0.10)
        for y in range(0, height, 3):
            pygame.draw.line(self.scanlineBase, (0, 255, 0, faint_alpha), (0, y), (width, y))

        # Prebuild the sweep gradient band (30px tall, alpha gradient)
        self.band_height = 30
        self.sweep_band = pygame.Surface((width, self.band_height), pygame.SRCALPHA)
        max_alpha = int(255 * 0.15)  # brighter at bottom
        for i in range(self.band_height):
            # Top of band: transparent, Bottom of band: max_alpha
            alpha = int(max_alpha * (i / self.band_height))
            color = (0, 255, 0, alpha)
            pygame.draw.line(self.sweep_band, color, (0, i), (width, i))

    def update(self):
        now = pygame.time.get_ticks()
        if not self.sweeping and now - self.lastSweep >= self.sweepInterval:
            self.sweeping = True
            self.startTime = now
        if self.sweeping and now - self.startTime >= self.sweepDuration:
            self.sweeping = False
            self.lastSweep = now

    def draw(self, surface):
        surface.blit(self.scanlineBase, (0, 0))
        if self.sweeping:
            elapsed = pygame.time.get_ticks() - self.startTime
            progress = elapsed / self.sweepDuration
            sweepY = int(progress * self.height)
            top = sweepY - self.band_height
            if top < 0:
                top = 0
            elif top + self.band_height > self.height:
                top = self.height - self.band_height
            surface.blit(self.sweep_band, (0, top))
