import pygame
from components import evolutions, hero
from images import upgrades
from stateManager.base import BaseState

counter = 2


class Upgrade(BaseState):
    def __init__(self):
        super().__init__()
        self.quit = None
        global counter
        self.active_index = 0  # Variable that holds if left/right key were pressed
        self.options = ["Left", "Right"]
        self.next_state = "BATTLE"
        evo = str(counter)
        self.left_image = pygame.image.load(f"{evo}.png").convert_alpha()
        counter += 1
        evo = str(counter)
        self.right_image = pygame.image.load(f"{evo}.png").convert_alpha()
        counter += 1
        self.image_width = 400
        self.image_height = 600
        self.left_rect = pygame.Rect(0, 0, self.image_width, self.image_height)
        self.right_rect = pygame.Rect(self.screen_rect.width - self.image_width, 0, self.image_width, self.image_height)

    def render_text(self, index):
        color = pygame.Color((203, 228, 222)) if index == self.active_index else pygame.Color((14, 131, 136))
        return self.font.render(self.options[index], True, color)

    def get_text_position(self, text, index):
        center = (self.screen_rect.center[0], self.screen_rect.center[1] + (index * 50))
        return text.get_rect(center=center)

    def handle_action(self):
        hero_inst = hero.Hero(500, 50, 0, 0)
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.K_LEFT:
            hero_inst = evolutions.upgrade(0)
            self.done = True
        elif event.key == pygame.K_RIGHT:
            hero_inst = evolutions.upgrade(2)
            self.done = True


    # Controls
    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.left_rect.collidepoint(event.pos):
                self.done = True
            elif self.right_rect.collidepoint(event.pos):
                self.quit = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.active_index = 1 if self.active_index <= 0 else 0
            elif event.key == pygame.K_LEFT:
                self.active_index = 0 if self.active_index >= 1 else 1
            elif event.key == pygame.K_RETURN:
                self.handle_action()

    def draw(self, surface):
        surface.fill(pygame.Color("black"))
        for index, option in enumerate(self.options):
            text_render = self.render_text(index)
            surface.blit(text_render, self.get_text_position(text_render, index))
        # draw the images
        surface.blit(self.left_image, self.left_rect)
        surface.blit(self.right_image, self.right_rect)

    def update(self):
        global counter
        counter += 1
        evo = str(counter)
        self.left_image = pygame.image.load(f"{evo}.png").convert_alpha()
        counter += 1
        evo = str(counter)
        self.right_image = pygame.image.load(f"{evo}.png").convert_alpha()
