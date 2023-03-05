import pygame
from .base import BaseState

class Splash(BaseState):
    def __init__(self):
        super(Splash, self).__init__()
        self.title = self.font.render("Root Game", True, pygame.Color((14, 131, 136)))  # Text
        self.title_rect = self.title.get_rect(center=self.screen_rect.center)   # Location on screen text generates
        self.next_state = "UPGRADE"
        self.time_active = 0

    # Update function keep splash screen open for 5 seconds
    def update(self, dt):
        self.time_active += dt
        if self.time_active >= 500:
            self.done = True
            
    def draw(self, surface):
        surface.fill(pygame.Color((44, 51, 51)))         # Background
        surface.blit(self.title, self.title_rect)   # Text generation