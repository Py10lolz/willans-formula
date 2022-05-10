# calculate nth-prime using Willans' formula
from math import floor, cos, factorial, pi

for n in range(1, 7):
	res = 1
	for i in range(1, 1+2**n):
		c = 0
		for j in range(1, 1+i):
			f = (factorial(j-1)+1)/j
			c += floor(cos(f*pi)**2)
		res += floor((n/c)**(1/n))
	print(f"the {n}th prime is {res}")
