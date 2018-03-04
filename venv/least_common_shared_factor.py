# calculate the smallest number divisible both by a and b (params passed to the function)


def least_common_shared_factor(a, b):
	
	base_val = 0
	least_common_start = 0
	other_val = 0
	counter = 1
	
	if a == 0 or b == 0:
		return False
	
	if a > b:
		base_val = a
		other_val = b
		
	elif a == b:
		return a
	
	else:
		base_val = b
		other_val = a
		
	while least_common_start <= a*b :
		
		least_common_start = base_val * counter

		if least_common_start % other_val == 0:
			return least_common_start
		else:
			counter = counter + 1
			
			
# some tests

