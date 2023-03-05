import pygame

# Initialise pygame
pygame.init()

# Set window size
size = width, height = 600, 600
screen = pygame.display.set_mode(size)

# Clock
clock = pygame.time.Clock()

# Load image
image = pygame.image.load('../images./binaryTree.jpg')

# Set the size for the image
DEFAULT_IMAGE_SIZE = (600, 600)

# Scale the image to your needed size
image = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)

# Set a default position
DEFAULT_IMAGE_POSITION = (0, 0)

# Prepare loop condition
running = False

# change the window screen title
pygame.display.set_caption('Decision Binary Tree')

WHITE = (255, 255, 255)
GREY = (69, 69, 69)
# Create a font file by passing font file
# and size of the font
font = pygame.font.SysFont('chalkduster.ttf', 25)
font2 = pygame.font.SysFont('chalkduster.ttf', 18)

C1 = WHITE  # Colors of each text
C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13, C14, C15 = \
    GREY, GREY, GREY, GREY, GREY, GREY, GREY, GREY, GREY, \
        GREY, GREY, GREY, GREY, GREY

# Render the texts that you want to display
text1 = font.render('Start', True, C1)

text2 = font.render('+ 80 Dmg', True, C2)
text3 = font.render('+ 30 Def', True, C3)

text4 = font2.render('+ 100 Dmg', True, C4)
text5 = font2.render('+ 30% Dodge', True, C5)
text6 = font2.render('+ 50 Dmg', True, C6)
text7 = font2.render('+ 50% Dodge', True, C7)

text8 = font2.render('+ 269 Dmg', True, C8)
text9 = font2.render('+ 40% Def', True, C9)
text10 = font2.render('+ 200 Dmg', True, C10)
text11 = font2.render('+ 40% Def', True, C11)
text12 = font2.render('+ 70 Def', True, C12)
text13 = font2.render('+ 40% Dodge', True, C13)
text14 = font2.render('+ 150 Dmg', True, C14)
text15 = font2.render('+ 40% Dodge', True, C15)

# create a rectangular object for the
# text surface object
textRect1 = text1.get_rect()
textRect2 = text2.get_rect()
textRect3 = text3.get_rect()
textRect4 = text4.get_rect()
textRect5 = text5.get_rect()
textRect6 = text6.get_rect()
textRect7 = text7.get_rect()
textRect8 = text8.get_rect()
textRect9 = text9.get_rect()
textRect10 = text10.get_rect()
textRect11 = text11.get_rect()
textRect12 = text12.get_rect()
textRect13 = text13.get_rect()
textRect14 = text14.get_rect()
textRect15 = text15.get_rect()

# setting center for the first text
textRect1.center = (310, 530)  # start
textRect2.center = (270, 470)  # left branch
textRect3.center = (350, 470)  # right branch
textRect4.center = (200, 380)
textRect5.center = (280, 360)
textRect6.center = (350, 375)
textRect7.center = (410, 390)

textRect8.center = (140, 310)
textRect9.center = (200, 245)
textRect10.center = (250, 230)
textRect11.center = (300, 250)
textRect12.center = (355, 220)
textRect13.center = (390, 260)
textRect14.center = (438, 280)
textRect15.center = (490, 325)

path1, path2, path3 = -1, -1, -1


def choice1(cho1):
    global path1, C2, C3
    path1 = cho1
    if path1 == 0:
        C2 = WHITE
    elif path1 == 1:
        C3 = WHITE
    render_text()

def choice2(cho2):
    global path2, C4, C5, C6, C7
    path2 = cho2
    if path1 == 0:
        if path2 == 0:
            C4 = WHITE
        elif path2 == 1:
            C5 = WHITE
    elif path1 == 1:
        if path2 == 0:
            C6 = WHITE
        elif path2 == 1:
            C7 = WHITE
    render_text()

def choice3(cho3):
    global path3, C8, C9, C10, C11, C12, C13, C14, C15
    path3 = cho3
    if path1 == 0:
        if path2 == 0:
            if path3 == 0:
                C8 = WHITE
            elif path3 == 1:
                C9 = WHITE
        elif path2 == 1:
            if path3 == 0:
                C10 = WHITE
            elif path3 == 1:
                C11 = WHITE
    elif path1 == 1:
        if path2 == 0:
            if path3 == 0:
                C12 = WHITE
            elif path3 == 1:
                C13 = WHITE
        elif path2 == 1:
            if path3 == 0:
                C14 = WHITE
            elif path3 == 1:
                C15 = WHITE
    render_text()

# Event loop
def render_text():
    # Render the texts that you want to display
    global text1, text2, text3, text4, text5, text6, text7, \
        text8, text9, text10, text11, text12, text13, text14, text15

    text1 = font.render('Start', True, C1)

    text2 = font.render('+ 80 Dmg', True, C2)
    text3 = font.render('+ 30 Def', True, C3)

    text4 = font2.render('+ 100 Dmg', True, C4)
    text5 = font2.render('+ 30% Dodge', True, C5)
    text6 = font2.render('+ 50 Dmg', True, C6)
    text7 = font2.render('+ 50% Dodge', True, C7)

    text8 = font2.render('+ 269 Dmg', True, C8)
    text9 = font2.render('+ 40% Def', True, C9)
    text10 = font2.render('+ 200 Dmg', True, C10)
    text11 = font2.render('+ 40% Def', True, C11)
    text12 = font2.render('+ 70 Def', True, C12)
    text13 = font2.render('+ 40% Dodge', True, C13)
    text14 = font2.render('+ 150 Dmg', True, C14)
    text15 = font2.render('+ 40% Dodge', True, C15)


def show_tree():
    running = False
    while not running:

        # Close window event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = True
        # Background Color
        screen.fill((255, 255, 255))

        # Show the image
        screen.blit(image, DEFAULT_IMAGE_POSITION)
        screen.blit(text1, textRect1)
        screen.blit(text2, textRect2)
        screen.blit(text3, textRect3)
        screen.blit(text4, textRect4)
        screen.blit(text5, textRect5)
        screen.blit(text6, textRect6)
        screen.blit(text7, textRect7)
        screen.blit(text8, textRect8)
        screen.blit(text9, textRect9)
        screen.blit(text10, textRect10)
        screen.blit(text11, textRect11)
        screen.blit(text12, textRect12)
        screen.blit(text13, textRect13)
        screen.blit(text14, textRect14)
        screen.blit(text15, textRect15)
        # Part of event loop
        pygame.display.flip()
        clock.tick(30)
