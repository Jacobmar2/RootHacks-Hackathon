class Boss:

    def __init__(self, x, y, img, health):
        #self.img = pygame.image.load('images/enemy.png')
        self.health = health
        self.rect.x = x
        self.rect.y = y
        self.counter = 0

    def uHealth(self, new_health):
        self.health = new_health
