# This is a game that follows a generation of heros battling a boss
# After each hero dies, their children evolve and take their place

# import modules
import pygame
import time

# initiate pygame screen
pygame.init()
screen = pygame.display.set_mode((800, 600))
done = False

def getScreen():
    return screen

# show welcome screen
# set the pygame window name
pygame.display.set_caption('Welcome!')

# create a surface object, image is drawn on it.
imp = pygame.image.load("images/welcome.png").convert()

# Using blit to copy content from one surface to other
screen.blit(imp, (0, 0))

# paint screen one time then wait 5s
pygame.display.flip()

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Flip the display
    pygame.display.flip()
    
# Done! Time to quit.
pygame.quit()
