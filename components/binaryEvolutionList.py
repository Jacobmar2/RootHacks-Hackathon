import hero, heroBattleTest

hero_instance = hero.hero(health, dmg, defence, dodge)


# upgrade function
def stats(first, second, third):
    # first choice
    if first == 0 and second == -1 and third == -1:
        return [130, 0, 0]
    elif first == 1 and second == -1 and third == -1:
        return [50, 30, 0]

    # second choice
    elif first == 0 and second == 0 and third == -1:
        return [230, 0, 0]
    elif first == 0 and second == 1 and third == -1:
        return [130, 0, 30]
    elif first == 1 and second == 0 and third == -1:
        return [100, 30, 0]
    elif first == 1 and second == 1 and third == -1:
        return [50, 30, 50]

    # third choice
    elif first == 0 and second == 0 and third == 0:
        return [499, 0, 0]
    elif first == 0 and second == 0 and third == 1:
        return [230, 40, 0]
    elif first == 0 and second == 1 and third == 0:
        return [330, 0, 30]
    elif first == 0 and second == 1 and third == 1:
        return [130, 40, 30]
    elif first == 1 and second == 0 and third == 0:
        return [100, 100, 0]
    elif first == 1 and second == 0 and third == 1:
        return [100, 30, 40]
    elif first == 1 and second == 1 and third == 0:
        return [200, 0, 50]
    elif first == 1 and second == 1 and third == 1:
        return [50, 30, 90]

    # if code breaks
    return -1


# upgrade = [dmg,def,dodge]
def upgrade(value):
    # define global variables
    global un, deux, tois
    # check which place value to add to
    if un == -1:
        un = value
    elif deux == -1:
        deux = value
    elif trois == -1:
        trois = value
    else:
        return -1


    statLst = stats(un, deux, trois)

    hero_instance.uDmg(statLst[0])
    hero_instance.uDefence(statLst[1])
    hero_instance.uDodge(statLst[2])


un = -1
deux = -1
trois = -1