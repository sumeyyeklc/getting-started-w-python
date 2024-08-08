colors = {"Red", "Yellow", "Blue", "Green","Purple"}
print(type(colors))
colors. add("Pink")
print(colors)
colors.remove("Pink")
print(colors)

set1 = {1,2,3,4,5}
set2 = {1,2,4,7,9,10}
print(set1.intersection(set2))
print(set1.union(set2))
print(set2.difference(set1))