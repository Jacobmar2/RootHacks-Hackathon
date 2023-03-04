import boss, hero, battleFunctions, evolutions

# initialize hero
hero_inst = hero.Hero(500, 50, 0, 0)
hero_inst.print_stats()
print("================")

# first evolution
hero_inst = evolutions.upgrade(1, -1, -1)
hero_inst.print_stats()
print("================")

# second evolution
hero_inst = evolutions.upgrade(1, 1, -1)
hero_inst.print_stats()
print("================")

# third evolution
hero_inst = evolutions.upgrade(1, 1, 1)
hero_inst.print_stats()
print("================")
