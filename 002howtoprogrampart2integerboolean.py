x, y, z = 1, 2, 3
print(x, y, z) #returns 1 2 3

def boolEx(a, b):
	print(type(a)) #returns <class 'bool'>
	print(a and b) #returns False
	print(a or b) #returns True
	print(not b) #returns True
	d = (1 > 2)
	print(d) #returns False
	d = ((2 > 1) and (3 <= 3))
	print(d) #returns True
boolEx(True, False)

import math, decimal

def intEx():
	'''integers, binary, octal base 8, hexadecimal base 16'''
	x = 5
	y = 2
	print("x + y =", x+y)
	print("{} + {} =".format(x, y), x+y) #returns 5 + 2 = 7
	print("{} - {} =".format(x, y), x-y) #returns 5 - 2 = 3
	print("{} * {} =".format(x, y), x*y) #returns 5 * 2 = 10
	print("{} / {} =".format(x, y), x/y) #returns 5 / 2 = 2.5
	print("{} % {} =".format(x, y), x%y) #returns 5 % 2 = 1
	print("{} ** {} =".format(x, y), x**y) #returns 5 ** 2 = 25
	print(float(x)) #returns 5.0
	print(pow(x,y)) #returns 25
	
	z = 100 / 3
	print(z)	
	print(type(z)) #returns <class 'float'>
	print(round(z,3)) #returns 33.333
	print(math.ceil(z)) #returns 34. need import math
	print(math.floor(z)) #returns 33. need import math

	zz = 1.234567891011121314151617
	print(zz) #returns 1.2345678910111213
	zz = decimal.Decimal("1.234567891011121314151617")
	print(zz) #returns 1.234567891011121314151617.  need import decimal
intEx()