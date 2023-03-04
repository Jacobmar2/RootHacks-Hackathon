import pygame

screen = pygame.display.set_mode((100, 100))

class Screen:
    def __init__(self, x, y):
        self.screen = pygame.display.set_mode((x, y))
        
    def getScreen():
        return screen

    def setScreen(x, y):
        screen = pygame.display.set_mode((x, y))