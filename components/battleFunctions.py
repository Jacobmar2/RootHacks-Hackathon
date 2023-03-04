# import modules
import random
import components.hero as hero, components.boss as boss


def battle(bossHlth, heroDmg, heroHlth, heroDef, heroDodge):
    # create an instance of hero class and boss class
    hero_instance = hero.hero(heroDmg, heroHlth, heroDef, heroDodge)
    boss_instance = boss.boss(bossHlth)

    heroHealth = heroHlth
    # hero deals damage (0-100)
    bossHealth = bossHlth - heroDmg
    # update boss class health

    # dodge (0-100)
    dodge = random.choice(range(0, 100))
    if dodge < heroDodge:
        return

    # boss deals random damage
    bossDmg = random.choice(range(50, 200))
    bossDmg = bossDmg - (bossDmg * (heroDef / 100))
    heroHealth -= bossDmg
    # update hero class health
    hero_instance.update_health(hero_instance.health - bossDmg)
    return
