import pygame
from .base import BaseState

class Victory(BaseState):
    def __init__(self):
        super(Victory, self).__init__()
        self.title = self.font.render("Victory", True, pygame.Color("white"))
        self.title_rect = self.title.get_rect(center=self.screen_rect.center)
        self.instructions = self.font.render("Press space to battle again, esc to quit", True, pygame.Color("white"))
        instructions_center = (self.screen_rect.center[0], self.screen_rect.center[1] +  50)
        self.instructions_rect = self.instructions.get_rect(center=instructions_center)

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                self.next_state = "UPGRADE"
                self.done = True
            elif event.key == pygame.K_ESCAPE:
                self.quit = True

    def draw(self, surface):
        surface.fill(pygame.Color((44, 51, 51)))
        surface.blit(self.title, self.title_rect)
        surface.blit(self.instructions, self.instructions_rect)