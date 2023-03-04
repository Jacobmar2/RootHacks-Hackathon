# This is a game that follows a generation of heros battling a boss
# After each hero dies, their children evolve and take their place

# import modules
import pygame
import sys
from stateManager import StateManager
from states.splashScreen import Splash
#from states.battleScreen import Battle
#from states.upgradeScreen import Upgrade
#from states.victoryScreen import Victory

# initiate pygame screen
pygame.init()
done = False

screen = pygame.display.set_mode((800,600))
states = {
    "SPLASH": Splash()
    #"BATTLE": Battle(),
    #"UPGRADE": Upgrade(),
    #"VICTORY": Victory()
}

stateManager = StateManager(screen, states, "SPLASH")
stateManager.run()

pygame.quit()
sys.exit
