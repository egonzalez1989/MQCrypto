from sage.all import *
from ..mq_bipolar import *

class UOV(MQBipolar):
	
	def __init__(self, q, o, v):
		super(UOV, self).__init__(q, o+v, o)
		self.o = o
		self.v = v
	
	def genQ(self):
		self.Q = []
		MS = MatrixSpace(self.Fq, self.v, self.n)
		VS = VectorSpace(self.Fq, self.n)
		for i in range(self.o):
			self.Q.append([MS.random_element(), VS.random_element(), self.Fq.random_element()])

	def genP(self):
		self.P = []
		A = self.T.A()
		At = A.submatrix(nrows = self.v).transpose()
		b = self.T.b()
		bt = b[:self.v]
		Xn = vector(self.PFqn.gens())
		for i in range(len(self.Q)):
			Mi = self.Q[i][0]
			vi = self.Q[i][1]
			ci = self.Q[i][2]
			MiA = Mi*A
			Mib = Mi*b
			self.P.append([At*MiA, At*Mib + bt*MiA + A.transpose()*vi, vi*b + bt*Mib + ci])
			
	def genS(self):
		pass

	def IQmap(self, Fqvec):
		count = 0
		found = False
		Xn = self.PFqn.gens()
		dXo = []
		for i in range(self.o):
			dXo.append({Xn[self.v+i]:1})
		while not found and count < 100:
			try:
				# Set random values to vinegar variables
				xv = []
				for i in range(self.v):
					xv.append(self.Fq.random_element())
				alpha = xv[:]
				alpha.extend(Xn[self.v:])
				alpha = vector(alpha)
				alpha = self.applyQuadMatrix(self.Q, alpha)
				
				A = []
				b = []
				for i in range(len(alpha)):
					A.append(map(lambda d: alpha[i].coefficient(d), dXo))
					b.append(alpha[i].constant_coefficient())
				A = matrix(self.Fq, A)
				b = vector(self.Fq, b) + Fqvec

				y = A.solve_right(b)
				xv.extend(y)

				found = True
			except ValueError:
				count += 1
				print 'Not'
		if (count == 100):
			raise ValueError('Solution not found')
		print('found: {}'.format(xv))
		return vector(xv)

	def ISmap(self, Fqvec):
		return Fqvec