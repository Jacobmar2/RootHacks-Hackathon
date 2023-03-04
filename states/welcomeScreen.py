import pygame
import screen

def showWelcome():
    # show welcome screen
    # set the pygame window name
    pygame.display.set_caption('Welcome!')

    # create a surface object, image is drawn on it.
    imp = pygame.image.load("images/welcome.png").convert()

    # Using blit to copy content from one surface to other
    screen.screen.blit(imp, (0, 0))

    # paint screen one time then wait 5s
    pygame.display.flip()