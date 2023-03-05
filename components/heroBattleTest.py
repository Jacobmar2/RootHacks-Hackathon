import boss, hero, battleFunctions, evolutions, displayTree

# initialize hero
hero_inst = hero.Hero(500, 50, 0, 0)
displayTree.show_tree()
hero_inst.print_stats()
print("================")
print("After each input, close the tree window to get to the next step")
print("================")

# first evolution
c1 = int(input("First choice, 1 for Right, 0 for Left\n"))
hero_inst = evolutions.upgrade(c1)
displayTree.choice1(c1)
displayTree.show_tree()
hero_inst.print_stats()
print("================")


# second evolution
c2 = int(input("Second choice, 1 for Right, 0 for Left\n"))
hero_inst = evolutions.upgrade(c2)
displayTree.choice2(c2)
displayTree.show_tree()
hero_inst.print_stats()
print("================")


# third evolution
c3 = int(input("Third choice, 1 for Right, 0 for Left\n"))
hero_inst = evolutions.upgrade(c3)
displayTree.choice3(c3)
displayTree.show_tree()
hero_inst.print_stats()
print("================")
