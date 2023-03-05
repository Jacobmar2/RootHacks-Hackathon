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
however = pygame.image.load("images/hardcode/fights/however.png")
victory = pygame.image.load("images/hardcode/fights/victory.png")
defeat = pygame.image.load("images/hardcode/fights/defeat.png")
gameOver = pygame.image.load("images/hardcode/fights/gameOver.png")
selection = [-1, -1, -1]
run = True
win = False
# ===================================== welcome screen =====================================
while run:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.blit(welcome, centre)
    # Update the display
    pygame.display.update()
    time.sleep(5)
    run = False

# ===================================== first battle =====================================
run = True
while run:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    hero_instance.print_stats()
    print("================")
    # Update the display
    screen.blit(firstFight, centre)
    pygame.display.update()
    win = battleFunctions.battle(100, 0, 0)
    time.sleep(4)
    run = False
# ===================================== Lose =====================================
if win:
    screen.blit(victory, centre)
    # Update the display
    pygame.display.update()
    while True:
        print("****************************** Victory ******************************")
screen.blit(defeat, centre)
# Update the display
pygame.display.update()
time.sleep(3)
# ===================================== second select/battle =====================================
run = True
while run:
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
                win = battleFunctions.battle(130, 0, 0)
                time.sleep(4)
                run = False
            elif event.key == pygame.K_RIGHT:
                selection[0] = 1
                hero_instance.print_stats()
                print("================")
                # Update the display
                screen.blit(thirdFight, centre)
                pygame.display.update()
                win = battleFunctions.battle(50, 30, 0)
                time.sleep(4)
                run = False
# ===================================== Lose =====================================
if win:
    screen.blit(victory, centre)
    # Update the display
    pygame.display.update()
    while True:
        print("****************************** Victory ******************************")
screen.blit(defeat, centre)
# Update the display
pygame.display.update()
time.sleep(4)
# ===================================== third battle =====================================
run = True
while run:
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
                    win = battleFunctions.battle(230, 0, 0)
                    time.sleep(4)
                    run = False
                    if win:
                        pass
                elif selection[0] == 1:
                    hero_instance.print_stats()
                    print("================")
                    # Update the display
                    screen.blit(fifthFight, centre)
                    pygame.display.update()
                    win = battleFunctions.battle(130, 0, 30)
                    time.sleep(4)
                    run = False
            elif event.key == pygame.K_RIGHT:
                selection[1] = 1
                if selection[0] == 0:
                    hero_instance.print_stats()
                    print("================")
                    # Update the display
                    screen.blit(sixthFight, centre)
                    pygame.display.update()
                    win = battleFunctions.battle(100, 30, 0)
                    time.sleep(4)
                    run = False
                elif selection[0] == 1:
                    hero_instance.print_stats()
                    print("================")
                    # Update the display
                    screen.blit(seventhFight, centre)
                    pygame.display.update()
                    win = battleFunctions.battle(50, 30, 50)
                    time.sleep(4)
                    run = False

# ===================================== Lose =====================================
if win:
    screen.blit(victory, centre)
    # Update the display
    pygame.display.update()
    while True:
        print("****************************** Victory ******************************")
screen.blit(defeat, centre)
# Update the display
pygame.display.update()
time.sleep(3)
# ===================================== fourth selection/battle =====================================
run = True
while run:
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
                        win = battleFunctions.battle(499, 0, 0)
                        time.sleep(4)
                        run = False
                    elif selection[0] == 1:
                        hero_instance.print_stats()
                        print("================")
                        # Update the display
                        screen.blit(ninthFight, centre)
                        pygame.display.update()
                        win = battleFunctions.battle(230, 40, 0)
                        time.sleep(4)
                        run = False
                elif selection[1] == 1:
                    if selection[0] == 0:
                        hero_instance.print_stats()
                        print("================")
                        # Update the display
                        screen.blit(tenthFight, centre)
                        pygame.display.update()
                        win = battleFunctions.battle(330, 0, 30)
                        time.sleep(4)
                        run = False
                    elif selection[0] == 1:
                        hero_instance.print_stats()
                        print("================")
                        # Update the display
                        screen.blit(eleventhFight, centre)
                        pygame.display.update()
                        win = battleFunctions.battle(130, 40, 30)
                        time.sleep(4)
                        run = False

            elif event.key == pygame.K_RIGHT:
                selection[2] = 1
                if selection[1] == 0:
                    if selection[0] == 0:
                        hero_instance.print_stats()
                        print("================")
                        # Update the display
                        screen.blit(twelfthFight, centre)
                        pygame.display.update()
                        win = battleFunctions.battle(100, 100, 0)
                        time.sleep(4)
                        run = False
                    elif selection[0] == 1:
                        hero_instance.print_stats()
                        print("================")
                        # Update the display
                        screen.blit(thirteenthFight, centre)
                        pygame.display.update()
                        win = battleFunctions.battle(100, 30, 40)
                        time.sleep(4)
                        run = False
                elif selection[1] == 1:
                    if selection[0] == 0:
                        hero_instance.print_stats()
                        print("================")
                        # Update the display
                        screen.blit(fourteenthFight, centre)
                        pygame.display.update()
                        win = battleFunctions.battle(200, 0, 50)
                        time.sleep(4)
                        run = False
                    elif selection[0] == 1:
                        hero_instance.print_stats()
                        print("================")
                        # Update the display
                        screen.blit(fifteenthFight, centre)
                        pygame.display.update()
                        win = battleFunctions.battle(50, 30, 90)
                        time.sleep(4)
                        run = False

# ===================================== game over =====================================
if win:
    screen.blit(victory, centre)
    # Update the display
    pygame.display.update()
    while True:
        print("****************************** Victory ******************************")
screen.blit(gameOver, centre)
# Update the display
pygame.display.update()
time.sleep(4)
screen.blit(however, centre)
# Update the display
pygame.display.update()
time.sleep(5)
# ===================================== Last Fight =====================================
run = True
while run:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.blit(lastFight, centre)
    # Update the display
    pygame.display.update()
    time.sleep(3)
    run = False

# ===================================== Win =====================================
if run == False:
    screen.blit(victory, centre)
    # Update the display
    pygame.display.update()
    while True:
        print("""*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-Victory-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                 -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*Victory*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-""")
