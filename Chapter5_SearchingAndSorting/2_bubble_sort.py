def bubble_sort(num_list: list, ascending=True):
	num_iteration = 0
	for i in range(len(num_list)):
		flag = True
		for j in range(1, len(num_list) - i):
			num_iteration += 1
			left = num_list[j-1] 
			right = num_list[j]
			
			if ascending:			
				if left > right:
					num_iteration += 1
					flag = False
					num_list[j-1] = right
					num_list[j] = left
			else:
				if left < right:
					num_iteration += 1
					flag = False
					num_list[j-1] = right
					num_list[j] = left
		if flag:
				print('number of iteration: %d' % num_iteration)
				return num_list
	print('number of iteration: %d' % num_iteration)
	return num_list

def main():
	test_list = [1,2,3,4,5,6,7,8,100,10]
	
	print("test_list: ")
	print(test_list)
	print()
	
	sorted_list = bubble_sort(test_list, ascending=True)
	
	print("sorted_list: ")
	print(sorted_list)

if __name__ == '__main__':
	main()