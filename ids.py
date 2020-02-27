from socket import *
from subprocess import check_output
from sys import argv

def xor (a,b):
	c = bytearray()
	for i in range(len(a)):
		c.append(a[i] ^ b[i % len(b)])
	return bytes(c)

if (len(argv) != 2):
	print ('Usage:\n\tpython3 %s [ip]' % argv[0])
	quit()
default_key = bytes.fromhex('0322A714BEC4102DF137C71E68492367')
s = socket()
s.connect((argv[1], 1337))
s.send(xor(('a'*4+'\x7e\x2a'+'a'*8).encode(), default_key))
enckey = s.recv(8, MSG_WAITALL)
key = b'a'*8 + xor(enckey, default_key)
s.send(xor(b'\xde\xad', key))

