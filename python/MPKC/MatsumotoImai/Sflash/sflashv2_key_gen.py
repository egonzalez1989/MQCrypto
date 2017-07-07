from sage.all import *
from ...variation import *
from ..mi_generator import MIKeyGenerator 
from .sflash_key_pair import *
from .sflash_key_scheme import *
import binascii

''' Class for generation of key pair for SFLASH scheme '''
class SflashKeyv2Generator(MIKeyGenerator):
	
	def __init__(self):
		self.scheme = Sflashv2()
		super(SflashKeyv2Generator, self).__init__(Sflashv2())