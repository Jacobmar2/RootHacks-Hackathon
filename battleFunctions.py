#import modules
import random
import hero, boss

def battle(bossHlth,heroDmg,heroHlth,heroDef,heroDodge):
    heroHealth = heroHlth
    # hero deals damage (0-100)
    bossHealth = bossHlth - heroDmg

    # dodge (0-100)
    dodge = random.choice(range(0,100))
    if dodge < heroDodge:
        return(heroHlth,bossHealth)

    # boss deals random damage
    bossDmg = random.choice(range(50,200))
    bossDmg = bossDmg - (bossDmg * (heroDef/100))
    heroHealth -= bossDmg

    return(heroHealth, bossHealth)
