class hero:
    def __init__(self, dmg, health, defence, dodge):
        self.dmg = dmg
        self.health = health
        self.defence = defence
        self.dodge = dodge

    def update_health(self, new_health):
        self.health = new_health
