from MPKC.UOV.uov import *
from MPKC.Utils.utils import *
import time

start = time.time()
q = 16
o = 40
v = 2*o
n = o+v

# args = {'q': q, 'o': o, 'v': v}
# genKeyPair('UOV', '/home/edgar/MQCrypto/python/keygen/uov_key', args)

scheme = UOV(q, o, v)
print('Object init: {}'.format(time.time()-start))

start = time.time()
scheme.init()
print('Key gen: {}'.format(time.time()-start))

start = time.time()
ba = sysToBin(scheme.P)
# print ''.join('{:02x}'.format(x) for x in ba)
print('Pub enc: {} - size: {}b'.format(time.time()-start, len(ba)))

start = time.time()
ba = sysToBin(scheme.Q)
ba.extend(affToBin(scheme.T))
print('Priv enc: {} - size: {}b'.format(time.time()-start, len(ba)))

vec = []
for i in range(o):
	vec.append(scheme.Fq.random_element())
vec = vector(scheme.Fq, vec)
start = time.time()
sign = scheme.privMap(vec)
print('Sign: {}'.format(time.time()-start))#, result - {}'.format(time.time()-start, sign))

start = time.time()
ver = scheme.pubMap(sign)
assert(vec == ver)
print('Verif: {}'.format(time.time()-start))

