from sage.all import *
from MPKC.MatsumotoImai.Sflash.sflashv1 import *
from MPKC.MatsumotoImai.Sflash.sflashv2 import *
from MPKC.UOV.uov import *
from MPKC.MatsumotoImai.matsumoto_imai import *
from MPKC.Utils.utils import *
import pickle

def genKeyPair(clazz, path, args = None):
	scheme = getInstance(clazz, args)
	scheme.init()
	fkey = open(path + '.priv', 'wb')
	if 'UOV' in clazz:
		ba = sysToBin(scheme.Q)
		ba.extend(affToBin(scheme.T))
	else:
		ba = affToBin(scheme.S)
		ba.extend(affToBin(scheme.T))
	lenBytes = intToBin(len(ba))
	fkey.write(intToBin(lenBytes))
	fkey.write(len(ba))
	fkey.write(ba)
	fkey.flush()
	fkey.close()
	fkey = open(path + '.pub', 'wb')
	ba = sysToBin(scheme.P)
	fkey.write(ba)
	fkey.flush()
	fkey.close()

def loadPubKey(clazz, path, args = None):
	fkey = open(path + '.pub', 'rb')
	ba = fkey.read()
	P = binToSys(ba)
	fkey.close()
	return P

def loadPrivKey():
	fkey = open(path + '.priv', 'rb')
	ba = fkey.read()
	if 'UOV' in clazz:
		Q = binToSys(scheme.Q)
		ba.extend(affToBin(scheme.T))
	else:
		ba = affToBin(scheme.S)
		ba.extend(affToBin(scheme.T))
	fkey.close()
	return P

def sign(clazz, path, Fqvec, args = None):
	scheme = getInstance(clazz, args)
	fkey = open(path + '.priv', 'r')
	ISA = pickle.load(fkey)
	ISb = pickle.load(fkey)
	if not 'Sflash' in clazz:
		scheme.Q = pickle.load(fkey)
	ITA = pickle.load(fkey)
	print ITA
	ITb = pickle.load(fkey)
	print ITb
	AG = AffineGroup(len(ISb), ISb[0].parent())
	scheme.IS = AG(ISA, ISb)
	scheme.IT = AG(ITA, ITb)
	sign = scheme.privMap(Fqvec)
	fkey.close()
	print sign
	return sign

def verify():

def getInstance(clazz, args = None):
	if 'MatsumotoImai' == clazz:
		scheme = MatsumotoImai(args['q'], args['n'], args['alpha'], args['h'])
		scheme.Fqn = Fqn
	elif 'UOV' == clazz:
		scheme = UOV(args['q'], args['o'], args['v'])
	else:
		scheme = globals()[clazz]()
	return scheme

# i = 0
# if (len( sys.argv ) < 2 ):
# 	print("More args required!\n")
# 	sys.exit(1)
# opt = sys.argv[i]
# i+=1
# clazz = sys.argv[i]
# i+=1
# path = sys.argv[i]

# Verificar que existe archivo (falta)
# if (opt == 'genkey'):
# 	genKeyPair(clazz, path)
# if (opt == 'sign'):
# 	signPath = path
# 	i+=1
# 	keyPath = sys.argv[i]


# 	idx = dir[::-1].find("/")
# 	if idx > 0:
# 		dir = dir[0: len(dir) - idx - 1]
# 		if not os.path.isdir(dir):
# 			print("Out file required!\n")
# 			sys.exit(1)
# else:
# 	filePath = dir + '/sflash'