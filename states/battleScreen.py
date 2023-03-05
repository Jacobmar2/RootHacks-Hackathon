import pygame
from .base import BaseState
from ..components.hero import Hero

class Battle(BaseState):
    def __init__(self):
        super(Battle, self).__init__()
        self.rect = pygame.Rect((0, 0), (80, 80))
        self.rect.center = self.screen_rect.center
        self.character = pygame.image.load('images/plantguy.png')
        self.character_spawn = self.character.get_rect(center=self.screen_rect.center)
        self.player = CharacterMovement(self.character, 10, 2.5)
        self.screen = pygame.display.get_surface()
        self.next_state = "VICTORY"

    def update(self, dt):
        pygame.display.get_surface().fill(pygame.Color((44, 51, 51)))
        self.player.move()
        pygame.display.get_surface().blit(self.player.image, self.player.pos)
        pygame.display.update()
        
class CharacterMovement:
    def __init__(self, image, height, speed):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(0, height)
        self.rect = image.get_rect()

        self.counter = 0

    def move(self):
        distance = 60

        if self.counter >= 0 and self.counter <= distance:
            self.pos.top += self.speed
        elif self.counter >= distance and self.counter <= distance*2:
            self.pos.top -= self.speed
        else:
            self.counter = 0

        self.counter += 1