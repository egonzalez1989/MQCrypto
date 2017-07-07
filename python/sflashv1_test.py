from MPKC.MatsumotoImai.Sflash.sflashv1 import *
import time

start = time.time()
scheme = Sflashv1()
print('Object init: {}'.format(time.time()-start))

start = time.time()
scheme.init()
print('Key gen: {}'.format(time.time()-start))

'''PFqn = PolynomialRing(scheme.Fq, 'X', 37)
Xn = PFqn.gens()
print Xn
vec = scheme.Qmap(Xn)
print('Q-S(X): ' + str(vec))'''

vec = vector(scheme.Fq, [1]*37)
for i in range(37):
	vec[i] = scheme.Fq.random_element()
start = time.time()
sign = scheme.privMap(vec)
print('Sign: time - {}, result - {}'.format(time.time()-start, sign))

start = time.time()
ver = scheme.pubMap(sign)
print('Verif: time - {}, result - {}'.format(time.time()-start, vec[:26] == ver))


'''print('v: ' + str(vec))

vec = scheme.Smap(vec)
print('S(v): ' + str(vec))
vec = scheme.Qmap(vec)
print('Q-S(v): ' + str(vec))
vec = scheme.Tmap(vec)
print('T-Q-S(v): ' + str(vec))


vec = scheme.ITmap(vec)
print('IT(v): ' + str(vec))
vec = scheme.IQmap(vec)
print('IQ-IT(v): ' + str(vec))
vec = scheme.ISmap(vec)
print('IS-IQ-IT(v): ' + str(vec))

vec = scheme.Pmap(vec)
print('P(v): ' + str(vec))
print(ver)'''