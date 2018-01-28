#The program implements RSA Cryptosystem algorithm with functions for key-generation
#RSA encryption and decryption algorithm
#find large primes of 1024 bits and calculate phi(N) euler totient 
#G(): key-generation pk =(N,e) sk = (N,d) [ed = 1 mod phi(N)] by Extended-euclid-algs
#F(pk,x)=RSA(x): x^e  mod N by Chinese Remainder Theorem
#F_inv(sk,y)=y^d mod N by Chinese Remainder Theorem
#Output the encrypted cipher or decrypt a cipher


import gmpy2
from gmpy2 import mpz
from gmpy2 import c_mod,powmod
from Crypto.Util import number 

def key_generator():
	len_prime = 1024
	p=number.getPrime(len_prime)
	q=number.getPrime(len_prime)

	N=p*q
	#taking e = F4 fermat prime 
	e = 65537

	#calculating d

	d = gmpy2.invert(e,phi(p,q))
	public  = (N,e) 
	private = (N,d)
	key = [public , private, p, q]
	return key

def phi(p,q):#Euler Totient
	return (p-1)*(q-1)
#calculate x^e mod N by chinese remainder theorem

def RSA_encrypt(x,e,N):
	xe=pow(mpz(x),e)
	cipher_Enc = c_mod(mpz(xe),N)+N
	return cipher_Enc

def RSA_decrypt(y,d,p,q):
	yd = powmod(mpz(y),d,p*q)
	message_Dec= chinese_rem(yd,p,q)
	return yd

def chinese_rem(x,m1,m2):
	a1 = c_mod(x,m1)+m1
	a2 = c_mod(x,m2)+m2
	M = m1*m2
	M1 = M/m1
	M2 = M/m2
	y1= gmpy2.invert(M1,m1)
	y2= gmpy2.invert(M2,m2)
	return (a1*M1*y1)+(a2*M2*y2) 


def main():
	keys = key_generator()
	public =keys[0]
	private=keys[1]
	p=keys[2]
	q=keys[3]
	e=public[1]
	N=public[0]
	d=private[1]
	message = "This is my secret message hello my name is debarghya."
	message_encoded = message.encode('hex')
	message_decimal = int(message_encoded,16)


	cipher=RSA_encrypt(message_decimal,e,N)



	message_decoded=RSA_decrypt(cipher,d,p,q)
	ENC=hex(message_decoded)
	hex_encoding = ENC[2:len(ENC)]
	print hex_encoding.decode('hex')



main()

