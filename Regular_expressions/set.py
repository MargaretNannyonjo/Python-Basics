set = {0, 1, 2, 3, 4, 5}
set.add(6)
print(set)

set1 = {1, 2, 3}
set2 = {3, 4, 5}

union = set1 | set2
intersection = set1 & set2
difference = set1 - set2

print("Union:", union)
print("Intersection", intersection)
print("Difference", difference)
