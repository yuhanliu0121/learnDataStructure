def find_sorted_pos(sorted_list: list, val):
	low = 0
	high = len(sorted_list) - 1
	while low < high:
		mid = (low + high) // 2
		
		if sorted_list[mid] == val:
			return mid
		
		if sorted_list[mid] < val:
			low = mid + 1
		else:
			high = mid - 1
			
	return low
	
def main():
	sorted_list = [1,4,6,7,9,11,15,18,21,25,28]
	print(find_sorted_pos(sorted_list, 28))
	
if __name__ == "__main__":
	main()