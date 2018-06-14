import gmpy2 
from gmpy2 import powmod,mpz,c_mod
from random import randint 

p=mpz(13710221545914561761)
q=mpz(11066328760152681859)

N = p*q

# q is 3 mod 4
# p is 1 mod 8


# SHANK ALGORITHM



a=1


e = 0
m = p 
t=m-1

def chinese_rem(x1,x2,m1,m2):
	a1 = c_mod(x1,m1)+m1
	a2 = c_mod(x2,m2)+m2
	M = m1*m2
	M1 = M/m1
	M2 = M/m2
	y1= gmpy2.invert(M1,m1)
	y2= gmpy2.invert(M2,m2)
	return (a1*M1*y1)+(a2*M2*y2)

while(True):
	if(t % 2 != 0):
		break
	e=e+1
	t=t/2

q = (m-1)/pow(2,e)


# generate quadratic non-residue of m
while(True):
	x = randint(2,m-1)
	z = powmod(x,q,m)
	if(powmod(z,mpz(pow(2,e-1)),m) != 1):
		break



y = z
r = e
x = powmod(a,(q-1)/2,m)
v = a*x % m
w = v*x % m

while(True):
	if(w == 1):
		break
	k=0
	while(True):
		if(powmod(w,mpz(pow(2,k)),m)==1):
			break	
		k = k + 1

	d = powmod(y,mpz(pow(2,r-k-1)),m)	
	y = powmod(d,2,m)
	r = k
	v = (d*v) % m
	w = (w*y) % m



r1 = v  
r2 = p-v

m=p

r3 = powmod(a,(m+1)/4,m)
r4 = N/p-r3

# for p
print r1
print r2

# for q 
print r3
print r4

p=p
q=N/p	

x1 = r1  
x2 = r3
print chinese_rem(x1,x2,p,q)

c1 = chinese_rem(x1,x2,p,q)

x1 = r1  
x2 = r4
print chinese_rem(x1,x2,p,q)

c2 = chinese_rem(x1,x2,p,q)

x1 = r2  
x2 = r3
print chinese_rem(x1,x2,p,q)

c3 = chinese_rem(x1,x2,p,q)

x1 = r2  
x2 = r4
print chinese_rem(x1,x2,p,q)

c4 = chinese_rem(x1,x2,p,q)

print "......................"
















