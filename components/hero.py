class hero:
    def __init__(self, health, dmg, defence, dodge):
        self.dmg = dmg
        self.health = health
        self.defence = defence
        self.dodge = dodge

    def uHealth(self, new_health):
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
