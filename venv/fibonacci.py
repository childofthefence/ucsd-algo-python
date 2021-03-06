fib_nums = [0, 1]

# place is how many fib numbers, starting at 1.  The 10th fib number is thus 34
# indices in fib_nums stars at 0 so to get F19 would use something like fib_nums[19]
# and would be the 20th fib number (despite 19 being the index)


def calc_fib(place):
	
	if place == 0:
		return 0
	elif place == 1:
		return 1
	if place > 1:
		
		for vals in range(2, place):
		
			fib_nums.append(fib_nums[vals-1] + fib_nums[vals-2])
	
	# print(fib_nums)
	return fib_nums[len(fib_nums)-1]


x_val_pass = 1000
x = calc_fib(x_val_pass)
x1 = fib_nums[(x_val_pass-1)]
print('Calc fib to {}th place is {} and the index of {} val is {} '.format(x_val_pass, x, (x_val_pass-1), x1))
print(x == x1)