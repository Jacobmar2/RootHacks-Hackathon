#import modules
import random
import components.hero as hero, components.boss as boss

def battle(bossHlth,heroDmg,heroHlth,heroDef,heroDodge):
    heroHealth = heroHlth
    # hero deals damage (0-100)
    bossHealth = bossHlth - heroDmg
    # update boss class health

    # dodge (0-100)
    dodge = random.choice(range(0,100))
    if dodge < heroDodge:
        return

    # boss deals random damage
    bossDmg = random.choice(range(50,200))
    bossDmg = bossDmg - (bossDmg * (heroDef/100))
    heroHealth -= bossDmg
    # update hero class health
    hero.update_health(hero.health - bossDmg)
    return
