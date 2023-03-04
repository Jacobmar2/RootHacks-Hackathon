import hero, heroBattleTest

hero_instance = hero.hero(health, dmg, defence, dodge)


# upgrade function
def upgrade(first, second, third):
    # first choice
    if first == 0 and second == -1:
        return [130, 0, 0]
    elif first == 1 and second == -1:
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


first = -1
second = -1
third = -1

# upgrade = [dmg,def,dodge]
stats = upgrade(first, second, third)
hero_instance.uDmg(stats[0])
hero_instance.uDefence(stats[1])
hero_instance.uDodge(stats[2])
