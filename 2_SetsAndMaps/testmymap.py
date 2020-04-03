from mymap import Map

map1 = Map()

print('map1 = ')
print(map1)
print()

print('add (\'a\',1), (\'b\',2), (\'c\',3), (\'d\',4) to map1')
map1.add('a', 1)
map1.add('b', 2)
map1.add('c', 3)
map1.add('d', 4)

print('map1 = ')
print(map1)
print()

print('add (\'b\',10)')
map1.add('b', 10)
print(map1)
print()

print('remove (\'c\',3) from map1')
map1.remove('c')
print(map1)
print()

print('get the value corresponding to \'b\'')
print(map1.valueOf('b'))
print()

print('get the value corresponding to \'z\'')
print(map1.valueOf('z'))
print()
