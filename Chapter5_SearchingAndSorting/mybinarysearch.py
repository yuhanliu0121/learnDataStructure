def binary_search(search_list, value):
	# the list should be in ascending order
	assert isinstance(search_list, list), "must input a list"
	pointer_low =0
	pointer_high=len(search_list) - 1
	
	while pointer_high >= pointer_low:
		pointer_mid = (pointer_low + pointer_high) // 2
		if search_list[pointer_mid] == value:
			return pointer_mid
		if search_list[pointer_mid] > value:
			pointer_high = pointer_mid - 1
		if search_list[pointer_mid] < value:
			pointer_low = pointer_mid + 1
	return None
    
    # omit 2 comma of if statement