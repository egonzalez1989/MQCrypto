from MPKC.UOV.uov import *
import time

start = time.time()
q = 2**16
o = 40
v = 2*o
n = o+v
scheme = UOV(q, o, v)
print('Object init: {}'.format(time.time()-start))

start = time.time()
scheme.init()
print('Key gen: {}'.format(time.time()-start))

vec = []
for i in range(o):
	vec.append(scheme.Fq.random_element())
vec = vector(scheme.Fq, vec)
start = time.time()
sign = scheme.privMap(vec)
print('Sign: time - {}, result - {}'.format(time.time()-start, sign))

start = time.time()
ver = scheme.pubMap(sign)
print('Verif: time - {}, result - {}'.format(time.time()-start, ver == vec))