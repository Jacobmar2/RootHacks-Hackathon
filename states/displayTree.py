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

# Render the texts that you want to display
text1 = font.render('Start', True, WHITE)

text2 = font.render('+ 80 Dmg', True, GREY)
text3 = font.render('+ 30 Def', True, WHITE)

text4 = font2.render('+ 100 Dmg', True, GREY)
text5 = font2.render('+ 30% Dodge', True, GREY)
text6 = font2.render('+ 50 Dmg', True, WHITE)
text7 = font2.render('+ 50% Dodge', True, GREY)

text8 = font2.render('+ 269 Dmg', True, GREY)
text9 = font2.render('+ 40% Def', True, GREY)
text10 = font2.render('+ 200 Dmg', True, GREY)
text11 = font2.render('+ 40% Def', True, GREY)
text12 = font2.render('+ 70 Def', True, GREY)
text13 = font2.render('+ 40% Dodge', True, WHITE)
text14 = font2.render('+ 150 Dmg', True, GREY)
text15 = font2.render('+ 40% Dodge', True, GREY)


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
textRect12 = text10.get_rect()
textRect13 = text11.get_rect()
textRect14 = text10.get_rect()
textRect15 = text11.get_rect()

# setting center for the first text
textRect1.center = (310, 530) #start
textRect2.center = (270, 470) #left branch
textRect3.center = (350, 470) #right branch
textRect4.center = (200, 380)
textRect5.center = (280, 360)
textRect6.center = (350, 375)
textRect7.center = (410, 390)

textRect8.center = (140, 310)
textRect9.center = (200, 245)
textRect10.center = (250, 230)
textRect11.center = (300, 250)
textRect12.center = (360, 220)
textRect13.center = (385, 260)
textRect14.center = (438, 280)
textRect15.center = (490, 320)


# Event loop
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