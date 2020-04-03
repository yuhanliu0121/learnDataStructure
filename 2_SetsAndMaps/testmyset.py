from myset import Set

set1 = Set()

print('set1 = ')
print(set1)
print()

print('add 1, 2, 3, 4 to set1')
set1.add(1)
set1.add(2)
set1.add(3)
set1.add(4)

print('set1 = ')
print(set1)
print()

print('remove 3 from set1')
set1.remove(3)
print(set1)
print()

print('create set2')
set2 = Set()
set2.add(1)
set2.add(2)
print('set2 = ')
print(set2)
print()

print('set1 == set2 ?')
print(set1 == set2)
print()

print('set1 interset set2')
print(set1.interset(set2))
print()

print('set1 union set2')
print(set1.union(set2))
print()

print('set1 difference set2')
print(set1.difference(set2))
print()

print('add 4 to set2')
set2.add(4)
print('set2 = ')
print(set2)
print()

print('set1 == set2 ?')
print(set1 == set2)


