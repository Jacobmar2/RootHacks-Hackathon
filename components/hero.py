class hero:
    def __init__(self, health, dmg, defence, dodge):
        self.dmg = dmg
        self.health = health
        self.defence = defence
        self.dodge = dodge

    def update_health(self, new_health):
        self.health = new_health

    def print_stats(self):
        print("Health = ", self.health)
        print("Damage = ", self.dmg)
        print("Defence = ", self.defence)
        print("Dodge = ", self.dodge)

    def uDmg(self, new_damage):
        self.damage = new_damage

    def uDefence(self, new_defence):
        self.defence = new_defence

    def uDodge(self, new_dodge):
        self.dodge = new_dodge
