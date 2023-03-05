# import modules
import random, time
import components.hero as hero, components.boss as boss


def battle(heroDmg, heroDef, heroDodge):
    # create an instance of hero class and boss class
    bossHealth = 1000
    heroHealth = 500

    while bossHealth > 0 and heroHealth > 0:
        # hero deals damage (0-100)
        bossHealth = bossHealth - heroDmg
        if bossHealth < 0:
            bossHealth = 0
        # update boss class health
        # boss_instance.uHealth(bossHealth)
        print(f"Boss Health: {bossHealth:.2f}")
        # dodge (0-100)
        dodge = random.choice(range(0, 100))
        if dodge < heroDodge:
            return

        # boss deals random damage
        bossDmg = random.choice(range(50, 200))
        bossDmg = bossDmg - (bossDmg * (heroDef / 100))
        heroHealth -= bossDmg
        if heroHealth < 0:
            heroHealth = 0
        # update hero class health
        # hero_instance.uHealth(hero_instance.health - bossDmg)
        print(f"Hero Health: {heroHealth:.2f}")
        print("..............")
        time.sleep(2)
    if heroHealth == 0:
        return False
    elif bossHealth == 0:
        return True