fib_nums = [0, 1]

def calc_fib(place):
	
	if place == 0:
		return 0
	elif place == 1:
		return 1
	if place > 1:
		
		for vals in range(2, place):
		
			fib_nums.append(fib_nums[vals-1] + fib_nums[vals-2])
	
	print(fib_nums)
	return fib_nums[len(fib_nums)-1]


calc_fib(10)
x = calc_fib(10)
print(x)