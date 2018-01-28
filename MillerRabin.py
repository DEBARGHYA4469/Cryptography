#This program is for Miller-Rabin primality testing....

import gmpy2
from gmpy2 import mpz,powmod
from random import randrange

N = mpz(16) # the candidate for prime testing
security = 10
# algorithm
# N-1 = (2^s)d find s,d
# take a security parameter times random from [2 to n-1] fermat little theorem 
# check if a^d != 1 mod n or a^(2^r*d)!=1 mod n raise flag for composite
# r ranges from 1 to d-1

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
		return "None"
	return N 




def prime(N):
	flag=0
	u=2
	while(u<N):
		if(N%u==0):
			flag=1
		u=u+1
	if flag ==0:
		return N


 


for i in range(1000):
	print prime(i+5),miller_rabin(i+5,20)