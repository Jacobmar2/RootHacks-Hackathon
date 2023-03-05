import pygame, components.evolutions, images.upgrades
from .base import BaseState

class Upgrade(BaseState):
    def __init__(self):
        super(Upgrade, self).__init__()
        self.active_index = 0   # Variable that holds if left/right key were pressed
        self.options = ["Left, Right"]
        self.next_state = "BATTLE"

    def render_text(self, index):
        color = pygame.Color("red") if index == self.active_index else pygame.Color("white")
        return self.font.render(self.options[index], True, color)

    def get_text_position(self, text, index):
        center = (self.screen_rect.center[0], self.screen_rect.center[1] + (index * 50))
        return text.get_rect(center=center)

    def handle_action(self):
        if self.active_index == 0:
            self.done = True
        elif self.active_index == 1:
            self.quit = True

    # Controls
    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if left_side.collidepoint(pygame.mouse.get_pos()):
                self.active_index = 0
                self.handle_action()
                self.done = True
            elif right_side.collidepoint(pygame.mouse.get_pos()):
                self.active_index = 1
                self.handle_action()


    def draw(self, surface):
        surface.fill("")


    def update(self, dt):
        self.draw()
