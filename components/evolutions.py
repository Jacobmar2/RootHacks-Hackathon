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
    # global first, second, third
    # if first == -1:
    #     first = value
    # elif second == -1:
    #     second = value
    # elif third == -1:
    #     third = value
    # create an instance of the hero class
    hero_instance = hero.Hero(0, 0, 0, 0)

    # update hero based on stats
    hero_instance.uHealth(new_health=500)
    statLst = stats(first, second, third)
    hero_instance.uDmg(new_damage=statLst[0])
    hero_instance.uDefence(new_defence=statLst[1])
    hero_instance.uDodge(new_dodge=statLst[2])
    return hero_instance

#
# first = -1
# second = -1
# third = -1
