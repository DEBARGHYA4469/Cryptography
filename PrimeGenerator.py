#generate a large prime number by miller rabin primality test

from random import getrandbits,randrange
import gmpy2
from gmpy2 import mpz,powmod

def miller_rabin(N,security):
	s = 0
	d = N-1

	while(d % 2 == 0):
		d = d//2
		s= s + 1 #count the powers of two

	# N-1 = d*(2^s)
	flag =0
	for _ in range(security):
		a = randrange(2,N-1)
		check  = powmod(a,d,N)
		if check == 1 or check == N-1:   #if this fails suppose go to line 30
			continue
		for _ in range(s-1):   
			check = powmod(check,2,N)
			if check == N-1:
				break
		else :
			flag = 1

	if flag == 1:
		return 0
	return 1 


while(1):
	xx = mpz(getrandbits(1024))
	if(miller_rabin(xx,10) == 1):
		print xx
		break


