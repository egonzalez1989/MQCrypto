from sage.all import *
from ..mq_bipolar import *

class MatsumotoImai(MQBipolar):

	def __init__(self, q, n, alpha, h):
		super(MatsumotoImai, self).__init__(q, n, n)
		self.alpha = alpha
		self.h = h
		self.Fqn = None # By now, set extenson in subclasses. Probably better find a Conway

	def genQ(self):
		return

	def genP(self):
		#PFqn = PolynomialRing(self.Fq, 'X', self.n)
		W = self.PFqn.extension(self.Fqn.modulus()).gen()

		Xi = vector(self.PFqn.gens())
		Wi = vector(map(lambda x: W**x, range(self.n)))

		# Affine transform S
		# SX = list(self.S.A()*Xi + self.S.b())
		# Compute central map using the table for X^(q^alpha)
		TX = list(self.Tmap(Xi))
		QTX = []
		powtab = self.getExpTable()
		for i in range(self.n):
			QTX.append(sum(map(lambda j: TX[j], powtab[i])))
		QTX = vector(((vector(QTX) * Wi) * (vector(TX) * Wi)).lift().coefficients())
		# Affine transform S
		P = self.Smap(QTX)
		self.P = P[:26]

	def getExpTable(self):
		raise NotImplementedError("Implement me!!")

	def IQmap(self, Fqvec):
		#Transform from k^n to K
		W = self.Fqn.gen()
		Wi = vector(map(lambda j: W**j, range(37)))
		B = vector(Fqvec) * Wi
 
        #Compute B^{h}
		A = B**(self.h)
        
        #Transform from K to k^n
		return vector(A.list())

	def Qmap(self, Fqvec):
		Qx = []
		powtab = self.getExpTable()
		for i in range(self.n):
			Qx.append(sum(map(lambda j: Fqvec[j], powtab[i])))
		
		W = self.Fqn.gen()
		q = self.Fq.order()
		Wi = vector(map(lambda x: W**x, range(37)))
		Qx = ((vector(Qx) * Wi) * (vector(Fqvec) * Wi)).lift().list()
		return Qx

		#Transform from k^n to K
'''		W = self.Fqn.gen()
		q = self.Fq.order()
		Wi = vector(map(lambda x: W**x, range(37)))
		B = vector(Fqvec) * Wi
 
        #Compute B^{h}
		A = B**(q**self.alpha+1)
        
        #Transform from K to k^n
		return vector(A.list())'''

'''	def init(self, Fq, Fqn, P, Q, S, T, IQ, IS, IT):
		super(MQBipolarScheme, self).__init__(Fq, P, Q, S, T, IQ, IS, IT)
		self.Fqn = Fqn	

	def genQ(self):
		# Try to read the Q map for faster computation
		self.loadQ()

	def miGenQ(self):
		Li = map(lambda x: 'L' + str(x), range(self.m))
		Li.append(str(Fqn.gen()))
		
		PRFq_d = PolynomialRing(Fq, vars)
		Li = PRFq_d.gens()
		T, Li = Li[-1], Li[:-1]
		
		Lbar = map(lambda x: x**self.q-x, Li)
		Lbar.append(Fqn.polynomial())
		QR = PRFq_d.quo(Lbar)
		
		Li = QR.gens()
		T, Li = Li[-1], vector(Li[:-1])
#		T = Li[-1]
#		Li = vector(Li[:-1])
		Ti = vector(map(lambda x: T**x, range(37)))
		
		# Quadratic map. Store it in order tp not to compute exp again
		Qbar = ((Li*Ti)**(q**alpha+1)).lift()
		
		FqXd = PolynomialRing(Fq, 'L', 37, order = 'invlex')
		Q = map(lambda x: FqXd(Qbar.coefficient({T:x})), range(37))
		
		self.invertQ()
		self.Q = Q

	def encodeQ(self):
		s = ''
		Xi = self.Q[0].parent().gens()
		n = len(Q)
		for i in range(n):
			p = self.Q[i]
			for j in range(n):
				for k in range(n):
					s = s + str(p.coefficient(Xi[j]*Xi[k]))
		return s

	def decodeQ(self):
		print len(s)
		q = 128
		alpha = 11
		n = 37
		Fq = GF(q, 'X', x**7+x+1)
		PRFq_n = PolynomialRing(Fq, 'X', n)
		Xi = PRFq_n.gens()
		Q = [PRFq_n(0)]*n
		for i in range(n):
			for j in range(n):
				for k in range(n):
					Q[i]  = Q[i] + int(s[37**2*i+37*j+k])*Xi[j]*Xi[k]
		self.Q = Q

	def loadQ(f = '', tries = 0):
		if f == '':
			f = 'MIQ_{}_{}_{}.txt'.format(q, n, m)
		import os.path	
		if os.path.exists(f):
			print f + ' exists'
			rfile = open(f, "r")
			s = rfile.read()
			self.Q = decodeQ(s)
			rfile.close()			
		elif tries == 0:
			self.miGenQ()
			self.storeQ()
			return loadQ(1)
		else:
			raise Error('Cannot store Q')

	def storeQ(f = ''):
		if f == '':
			f = 'MIQ_{}_{}_{}.txt'.format(q, n, m)
		s = self.encodeQ(self.Q)
		wfile = open(f, 'w')
		wfile.write(s)
		wfile.close()'''