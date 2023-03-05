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