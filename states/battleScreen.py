import pygame
from .base import BaseState

class Battle(BaseState):
    def __init__(self):
        super(Battle, self).__init__()
        self.rect = pygame.Rect((0, 0), (80, 80))
        self.rect.center = self.screen_rect.center
        self.character = pygame.image.load('images/plantguy2.png')
        self.character_spawn = self.character.get_rect(center=self.screen_rect.center)
        self.x = 0
        self.y = 0
        self.o = PlaceholderMovement(self.character, self.y, 10)
        self.screen = pygame.display.get_surface()
        self.next_state = "VICTORY"
        
    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.o.move(up=True)
            if event.key == pygame.K_DOWN:
                self.o.move(down=True)
            if event.key == pygame.K_LEFT:
                self.o.move(left=True)
            if event.key == pygame.K_RIGHT:
                self.o.move(right=True)
            if event.key == pygame.K_SPACE:
                self.done = True

    def update(self, dt):
        pygame.display.get_surface().fill(pygame.Color("black"))
        self.o.move()
        pygame.display.get_surface().blit(self.o.image, self.o.pos)
        pygame.display.update()
        
class PlaceholderMovement:
    def __init__(self, image, height, speed):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(0, height)
        
    def move(self, up=False, down=False, left=False, right=False):
        if right:
            self.pos.right += self.speed
        if left:
            self.pos.right -= self.speed
        if down:
            self.pos.top += self.speed
        if up:
            self.pos.top -= self.speed