#load('mi_key_pair.sage')
from sage.all import *
from .mi_key_pair import *

''' Class for generation of Matsumoto-Imai key pairs. It is required to know the base field (coefficients) and the extension field
'''
class MIKeyGenerator(MQBipolarKeyGenerator):
	super(MIKeyGenerator, self).__init__(MatsumalphaotoImai())

def genKeyPair(self):
	keyPair = super(MIKeyGenerator, self).genKeyPair()
	keyPair.addParam('alpha', alpha)
	keyPair.addParam('h', h)