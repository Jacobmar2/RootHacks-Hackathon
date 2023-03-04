import hero


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
def upgrade(first, second, third):
    # create an instance of the hero class
    hero_instance = hero.hero(0, 0, 0, 0)
    hero_instance.uHealth(500)

    # update hero based on stats
    statLst = stats(first, second, third)
    hero_instance.uDmg(statLst[0])
    hero_instance.uDefence(statLst[1])
    hero_instance.uDodge(statLst[2])
