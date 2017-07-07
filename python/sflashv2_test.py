from MPKC.MatsumotoImai.Sflash.sflashv2 import *
import time

start = time.time()
scheme = Sflashv2()
print('Object init: {}'.format(time.time()-start))

start = time.time()
scheme.init()
print('Key gen: {}'.format(time.time()-start))

vec = vector(scheme.Fq, [1]*37)
for i in range(37):
	vec[i] = scheme.Fq.random_element()
start = time.time()
sign = scheme.privMap(vec)
print('Sign: time - {}, result - {}'.format(time.time()-start, sign))

start = time.time()
ver = scheme.pubMap(sign)
print('Verif: time - {}, result - {}'.format(time.time()-start, vec[:26] == ver))