class hero:
    def __init__(self, dmg, health, defence, dodge):
        self.dmg = dmg
        self.health = health
        self.defence = defence
        self.dodge = dodge

    def update_health(self, new_health):
        self.health = new_health

    def print_stats(self):
        print("Health = " , self.health)
        print("Damage = " , self.dmg)
        print("Defence = " , self.defence)
        print("Dodge = " , self.dodge)

    def decision(self, choice):
        # choice is boolean, yes is right, no is left
        print("Make your choice. Left button for +80 damage, Right button for +30 defence")
        if choice:
            self.defence += 30
        else:
            self.dmg += 80

    def decision2(self, choice2):
        if self.choice:  # right side
            print("Make your choice. Left button for +50 damage, Right button for +50 dodge")
            if self.choice2:
                self.dodge += 50
            else:
                self.dmg += 50
        else:
            print("Make your choice. Left button for +100 damage, Right button for +30 dodge")
            if choice2:
                self.dodge += 30
            else:
                self.dmg += 100

    def decision3(self, choice3):
        if self.choice:
            if self.choice2:
                print("Make your choice. Left button for +150 damage, Right button for +40 dodge")
                if self.choice3:
                    self.dodge += 40
                else:
                    self.dmg += 150
            else:
                print("Make your choice. Left button for +70 defence, Right button for +40 dodge")
                if self.choice3:
                    self.dodge += 40
                else:
                    self.defence += 70
        else:
            if self.choice2:
                print("Make your choice. Left button for +200 damage, Right button for +40 defence")
                if self.choice3:
                    self.defence += 40
                else:
                    self.dmg += 200
            else:
                print("Make your choice. Left button for +269 damage, Right button for +40 defence")
                if self.choice3:
                    self.defence += 40
                else:
                    self.dmg += 269
