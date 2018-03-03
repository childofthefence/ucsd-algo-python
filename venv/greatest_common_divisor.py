# calculates the gcd(a, b) of any two integers even negative integers


def gcd(a, b):
	
	start_point = 0
	if a > b:
		start_point = b
	elif a == b:
		return a
	elif a < b:
		start_point = a
		
	for vals in range(start_point, 1, -1):

		if a % vals == 0 and b % vals == 0:
			
			return vals


print gcd(10, 4)
print gcd(483, 567)
print gcd(645868, 2647)
