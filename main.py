# This is a game that follows a generation of heros battling a boss
# After each hero dies, their children evolve and take their place

# import modules
import pygame
import time

# initiate pygame screen
pygame.init()
screen = pygame.display.set_mode((600, 600))
done = False

# show welcome screen
# set the pygame window name
pygame.display.set_caption('Welcome!')

# create a surface object, image is drawn on it.
imp = pygame.image.load("images/welcome.png").convert()

# Using blit to copy content from one surface to other
screen.blit(imp, (0, 0))

# paint screen one time then wait 5s
pygame.display.flip()
status = True
while (status):

    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for i in pygame.event.get():

        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if i.type == pygame.QUIT:
            status = False
time.sleep(5)
