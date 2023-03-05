class Hero:
    def __init__(self, health, dmg, defence, dodge):
        self.dmg = dmg
        self.health = health
        self.defence = defence
        self.dodge = dodge

    def uHealth(self, new_health):
        if new_health < 0:
            self.health = 0
        self.health = new_health

    def uDmg(self, new_damage):
        self.dmg = new_damage

    def uDefence(self, new_defence):
        self.defence = new_defence

    def uDodge(self, new_dodge):
        self.dodge = new_dodge

    def print_stats(self):
        print("Health = ", self.health)
        print("Damage = ", self.dmg)
        print("Defence = ", self.defence)
        print("Dodge = ", self.dodge)


    # Nested Health Bar Class
    # class Healthbar(pygame.sprite, Sprite):
    #     def __init__(self):
    #         super().__init__()
    #         self.image = pygame.Surface((400, 400))
    #         self.image.fill((240, 240, 240))
    #         self.rect = self.image.get_rect(centre=(400, 400))
    #         self.current_health =
    #         self.maximum_health = 500
    #         self.health_bar_length = 250
    #         self.health_ratio = self.maximum_health / self.health_bar_length
    #
    #     def update(self):
    #         pass
