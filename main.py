# This is a game that follows a generation of heros battling a boss
# After each hero dies, their children evolve and take their place

# import modules
import pygame

# initiate pygame screen
pygame.init()
screen = pygame.display.set_mode((400, 500))

# Stops window from closing without user input
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()