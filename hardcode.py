# ignore

import pygame
import time
from components import hero, boss, battleFunctions

# Initialize Pygame
pygame.init()

# Set the size of the display screen
screen = pygame.display.set_mode((800, 600))

# initialize variables
hero_instance = hero.Hero(500, 50, 0, 0)
welcome = pygame.image.load("images/hardcode/welcome.png")
firstSelect = pygame.image.load("images/hardcode/1.png")
secondSelect = pygame.image.load("images/hardcode/2.png")
thirdSelect = pygame.image.load("images/hardcode/3.png")
fourthSelect = pygame.image.load("images/hardcode/4.png")
fifthSelect = pygame.image.load("images/hardcode/5.png")
sixthSelect = pygame.image.load("images/hardcode/6.png")
seventhSelect = pygame.image.load("images/hardcode/7.png")
centre = (0, 0)
firstFight = pygame.image.load("images/hardcode/fights/1.png")
secondFight = pygame.image.load("images/hardcode/fights/2.png")
thirdFight = pygame.image.load("images/hardcode/fights/3.png")
fourthFight = pygame.image.load("images/hardcode/fights/4.png")
fifthFight = pygame.image.load("images/hardcode/fights/5.png")
sixthFight = pygame.image.load("images/hardcode/fights/6.png")
seventhFight = pygame.image.load("images/hardcode/fights/7.png")
eighthFight = pygame.image.load("images/hardcode/fights/8.png")
ninthFight = pygame.image.load("images/hardcode/fights/9.png")
tenthFight = pygame.image.load("images/hardcode/fights/10.png")
eleventhFight = pygame.image.load("images/hardcode/fights/11.png")
twelfthFight = pygame.image.load("images/hardcode/fights/12.png")
thirteenthFight = pygame.image.load("images/hardcode/fights/13.png")
fourtheenthFight = pygame.image.load("images/hardcode/fights/14.png")
fifteenthFight = pygame.image.load("images/hardcode/fights/15.png")
lastFight = pygame.image.load("images/hardcode/fights/naruto.png")
selection = [-1, -1, -1]
# ===================================== welcome screen =====================================
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.blit(welcome, centre)
    # Update the display
    pygame.display.update()
    time.sleep(3)
    break

# ===================================== first battle =====================================
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    hero_instance.print_stats()
    print("================")
    screen.blit(firstFight, centre)
    # Update the display
    pygame.display.update()
    time.sleep(8)
    break
# ===================================== Win/Lose =====================================

# ===================================== second battle =====================================
while True:
    screen.blit(firstSelect, centre)
    # Update the display
    pygame.display.update()

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                selection[0] = 0
                hero_instance.print_stats()
                print("================")
                # Update the display
                screen.blit(secondFight, centre)
                pygame.display.update()
                time.sleep(8)
                break
            elif event.key == pygame.K_RIGHT:
                selection[0] = 1
                hero_instance.print_stats()
                print("================")
                # Update the display
                screen.blit(thirdFight, centre)
                pygame.display.update()
                time.sleep(8)
                break
# ===================================== win/lose =====================================

# ===================================== third battle =====================================
while True:
    if selection[0] == 0:
        # Update the display
        screen.blit(secondSelect, centre)
        pygame.display.update()

    elif selection[0] == 1:
        # Update the display
        screen.blit(thirdSelect, centre)
        pygame.display.update()

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                selection[1] = 0
                if selection[0] == 0:
                    hero_instance.print_stats()
                    print("================")
                    # Update the display
                    screen.blit(fourthFight, centre)
                    pygame.display.update()
                    time.sleep(8)
                    break
                elif selection[0] == 1:
                    hero_instance.print_stats()
                    print("================")
                    # Update the display
                    screen.blit(fifthFight, centre)
                    pygame.display.update()
                    time.sleep(8)
                    break
            elif event.key == pygame.K_RIGHT:
                selection[1] = 1
                if selection[0] == 0:
                    hero_instance.print_stats()
                    print("================")
                    # Update the display
                    screen.blit(sixthFight, centre)
                    pygame.display.update()
                    time.sleep(8)
                    break
                elif selection[0] == 1:
                    hero_instance.print_stats()
                    print("================")
                    # Update the display
                    screen.blit(seventhFight, centre)
                    pygame.display.update()
                    time.sleep(8)
                    break

# ===================================== win/lose =====================================

# ===================================== fourth battle =====================================
while True:
    if selection[0] == 0:
        if selection[1] == 0:
            # Update the display
            screen.blit(fourthSelect, centre)
            pygame.display.update()
        elif selection[1] == 1:
            # Update the display
            screen.blit(fifthSelect, centre)
            pygame.display.update()

    elif selection[0] == 1:
        if selection[1] == 0:
            # Update the display
            screen.blit(sixthSelect, centre)
            pygame.display.update()
        elif selection[1] == 1:
            # Update the display
            screen.blit(seventhSelect, centre)
            pygame.display.update()

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                selection[2] = 0
                if selection[1] == 0:
                    if selection[0] == 0:
                        hero_instance.print_stats()
                        print("================")
                        # Update the display
                        screen.blit(eighthFight, centre)
                        pygame.display.update()
                        time.sleep(8)
                        break
                    elif selection [0] == 1:
                        hero_instance.print_stats()
                        print("================")
                        # Update the display
                        screen.blit(ninthFight, centre)
                        pygame.display.update()
                        time.sleep(8)
                        break
                elif selection[1] == 1:
                    if selection[0] == 0:
                        hero_instance.print_stats()
                        print("================")
                        # Update the display
                        screen.blit(tenthFight, centre)
                        pygame.display.update()
                        time.sleep(8)
                        break
                    elif selection [0] == 1:
                        hero_instance.print_stats()
                        print("================")
                        # Update the display
                        screen.blit(eleventhFight, centre)
                        pygame.display.update()
                        time.sleep(8)
                        break

            elif event.key == pygame.K_RIGHT:
                selection[2] = 1
                if selection[1] == 0:
                    if selection[0] == 0:
                        hero_instance.print_stats()
                        print("================")
                        # Update the display
                        screen.blit(twelfthFight, centre)
                        pygame.display.update()
                        time.sleep(8)
                        break
                    elif selection[0] == 1:
                        hero_instance.print_stats()
                        print("================")
                        # Update the display
                        screen.blit(thirteenthFight, centre)
                        pygame.display.update()
                        time.sleep(8)
                        break
                elif selection[1] == 1:
                    if selection[0] == 0:
                        hero_instance.print_stats()
                        print("================")
                        # Update the display
                        screen.blit(fourteenthFight, centre)
                        pygame.display.update()
                        time.sleep(8)
                        break
                    elif selection[0] == 1:
                        hero_instance.print_stats()
                        print("================")
                        # Update the display
                        screen.blit(fifteenthFight, centre)
                        pygame.display.update()
                        time.sleep(8)
                        break
