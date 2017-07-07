from sage.all import *
from .key_pair import *

class MQBipolarKeyGenerator(object):

	def __init__(self, scheme):
		self.scheme = scheme

	def genKeyPair(self):
		self.scheme.init()
		keyPair = KeyPair(PublicKey({'P': self.P}), PrivateKey({'S': self.scheme.S}, {'T', self.scheme.T},
			{'Q': self.scheme.Q}, {'IS': self.scheme.IS}, {'IT': self.scheme.IT}, {'IQ': self.scheme.IQ}))
		return KeyPair