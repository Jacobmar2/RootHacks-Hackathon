class hero:
    def __init__(self, dmg, health, defence, dodge):
        self.dmg = dmg
        self.health = health
        self.defence = defence
        self.dodge = dodge

    def update_health(self, new_health):
        self.health = new_health

    def start(self):
        self.health = 500
        self.dmg = 50
        self.defence = 0
        self.dodge = 0

    def decision(self, choice):
        # choice is boolean, yes is right, no is left
        if choice:
            self.defence += 30
        else:
            self.dmg += 80

    def decision2(self, choice2):
        if self.choice: #right side
            if self.choice2:
                self.dodge += 50
            else:
                self.dmg += 50
        else:
            if choice2:
                self.dodge += 30
            else:
                self.dmg += 100

    def decision3(self, choice3):
        if self.choice:
            if self.choice2:
                if self.choice3:
                    self.dodge += 40
                else:
                    self.dmg += 150
            else:
                if self.choice3:
                    self.dodge += 40
                else:
                    self.defence += 70
        else:
            if self.choice2:
                if self.choice3:
                    self.defence += 40
                else:
                    self.dmg += 200
            else:
                if self.choice3:
                    self.defence += 40
                else:
                    self.dmg += 269
