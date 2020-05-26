# O(n) time
def merge_sorted_list(list1: list, list2: list):
	n1 = len(list1) - 1
	n2 = len(list2) - 1
	
	idx1 = 0
	idx2 = 0
	
	new_list = list()
	
	while idx1 <= n1 and idx2 <= n2:
		if list1[idx1] <= list2[idx2]:
			new_list.append(list1[idx1])
			idx1 += 1
		else:
			new_list.append(list2[idx2])
			idx2 += 1

	if idx1 > n1:
		new_list.extend(list2[idx2:])
	else:
		new_list.extend(list1[idx1:])
	return new_list
	
def main():
	list1 = [1,2,5,6,8,9,10,15,16,18,20,22,28]
	list2 = [2,6,8,9,10,158,165]
	
	print("list1:\n %s" % str(list1))
	print("\nlist2:\n %s" % str(list2))
	print("\nmerge_sorted_list:\n %s" % str(merge_sorted_list(list1, list2)))
	
if __name__ == "__main__":
	main()


