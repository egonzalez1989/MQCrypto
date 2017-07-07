''' Base class for a PKC Public Key
	Lazy for thinking good key classes. Maybe better implementation later
	All data for keys implemented as a dictionary
'''
class Key(object):
	def __init__(self, params):
		self.params = params
	
	def getEncoded(self):
		NotImplementedError( "Should have implemented this")

	def addParam(self, name, value):
		self.params[name] = value
	
	def addParams(self, namesValues):
		if (type(namesValues) != dict):
			raise Error("Don't know")
		self.params.update(namesValues)

	def getParam(self, name):
		return self.params[name]

	def getParams(self, namesValues):
		return self.params
''' Base class for a PKC Private Key
'''
class PrivateKey(Key):
	def __init__(self, params):
		super(PrivateKey, self).__init__(params)

class PublicKey(Key):
	def __init__(self):
		super(PublicKey, self).__init__(params)
    
''' Base class for a PKC KeyPair
'''
class KeyPair(object):
	def __init__(self, pubKey, privKey):
		self.public = pubKey
		self.private = privKey

	def getPublic(self):
		return self.public

	def getPrivate(self):
		return self.private

	def setPublic(self):
		self.public = public
    
	def setPrivate(self, private):
		self.private = private
