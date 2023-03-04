import boss, hero, battleFunctions, evolutions

#initialize hero
hero_inst = hero.hero(500, 50, 0, 0)
hero_inst.print_stats()
print("================")

# first evolution
evolutions.upgrade(1)
hero_inst.print_stats()
print("================")

# second evolution
evolutions.upgrade(1)
hero_inst.print_stats()
print("================")

# third evolution
evolutions.upgrade(1)
hero_inst.print_stats()
print("================")