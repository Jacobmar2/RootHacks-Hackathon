# This is a game that follows a generation of heros battling a boss
# After each hero dies, their children evolve and take their place

# import modules
import pygame
import time
import screen
import welcomeScreen

# initiate pygame screen
pygame.init()
done = False

screen.setScreen(800, 600)

# Run until the user asks to quit
running = True
while running:

    welcomeScreen.showWelcome()
    
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Flip the display
    pygame.display.flip()
    
# Done! Time to quit.
pygame.quit()
