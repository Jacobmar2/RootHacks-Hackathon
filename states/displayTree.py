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

# Create a font file by passing font file
# and size of the font
font1 = pygame.font.SysFont('freesanbold.ttf', 50)
font2 = pygame.font.SysFont('chalkduster.ttf', 20)

# Render the texts that you want to display
text1 = font1.render('GeeksForGeeks', True, (0, 255, 0))
text2 = font2.render('GeeksForGeeks', True, (0, 255, 0))

# create a rectangular object for the
# text surface object
textRect1 = text1.get_rect()
textRect2 = text2.get_rect()

# setting center for the first text
textRect1.center = (250, 250)

# setting center for the second text
textRect2.center = (250, 300)


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

    # Part of event loop
    pygame.display.flip()
    clock.tick(30)