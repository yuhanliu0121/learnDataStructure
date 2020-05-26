def ins_sort(num_list: list, ascending=True):
	n = len(num_list)
	
	for i in range(1, n):
		val = num_list[i]
		pos = i
		
		if ascending:
			while val < num_list[pos - 1] and pos > 0:
				num_list[pos] = num_list[pos - 1]
				num_list[pos - 1] = val 
				pos -= 1
		else:
			while val > num_list[pos-1] and pos > 0:
				num_list[pos] = num_list[pos - 1]
				num_list[pos - 1] = val 
				pos -= 1
	return num_list
	
	
def main():
	num_list = [1, 3, 2, 6, 6, 41, 5, 8, 4132, 6, 54, 2, 36, 6, 71, 2, 69, 56, 1, 47, 895, 1]
	
	print('before: ')
	print(num_list)
	
	print('\nafter: ')
	print(ins_sort(num_list,False))
	
if __name__ == '__main__':
	main()
