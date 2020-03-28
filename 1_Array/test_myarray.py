from myarray import Array

#===============Test Array==============

array = Array(5)

print("test getitem and set item")
for i in range(len(array)):
	array[i] = i

print("test iteration")
for i in array:
    print(i)
