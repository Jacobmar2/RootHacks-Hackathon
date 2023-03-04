class Boss:
    def __init__(self, x, y, health):
        self.health = health
        self.rect.x = x
        self.rect.y = y
        self.counter = 0

    def uHealth(self, new_health):
        self.health = new_health

    def move(self):
        distance = 80
        speed = 8

        if self.counter >= 0 and self.counter <= distance:
            self.rect.x += speed
        elif self.counter >= distance and self.counter <= distance*2:
            self.rect.x -= speed
        else:
            self.counter = 0

        self.counter += 1
