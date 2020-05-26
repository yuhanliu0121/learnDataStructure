def sel_sort(num_list: list, ascending=True):
	n = len(num_list)
	for i in range(n):
		temp_m = num_list[i]
		temp_idx = i
		for j in range(i + 1, n):
			if ascending: 
				if num_list[j] < temp_m:
					temp_m = num_list[j]
					temp_idx = j
			else:
				if num_list[j] > temp_m:
					temp_m = num_list[j]
					temp_idx = j
		
		if temp_idx != i:			
			temp = num_list[i]
			num_list[i] = num_list[temp_idx]
			num_list[temp_idx] = temp
	return num_list
	
def main():
	num_list = [1, 3, 2, 6, 6, 41, 5, 8, 4132, 6, 54, 2, 36, 6, 71, 2, 69, 56, 1, 47, 895, 1]
	
	print('before: ')
	print(num_list)
	
	print('\nafter: ')
	print(sel_sort(num_list))
	
if __name__ == '__main__':
	main()
		
		