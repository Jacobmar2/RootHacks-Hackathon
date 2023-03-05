import boss, hero, battleFunctions, evolutions, displayTree

# initialize hero
hero_inst = hero.Hero(500, 50, 0, 0)
displayTree.show_tree()
hero_inst.print_stats()
print("================")



# first evolution
hero_inst = evolutions.upgrade(1)
displayTree.choice1(1)
displayTree.show_tree()
hero_inst.print_stats()
print("================")


# second evolution
hero_inst = evolutions.upgrade(1)
displayTree.choice2(1)
displayTree.show_tree()
hero_inst.print_stats()
print("================")


# third evolution
hero_inst = evolutions.upgrade(1)
displayTree.choice3(1)
displayTree.show_tree()
hero_inst.print_stats()
print("================")
