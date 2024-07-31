import numpy

from dataclasses import dataclass

@dataclass
class Dynamic:
	"""PRODUCTION-INJECTION-INFLUX PARAMETERS

	Np 		: Cumulative oil produced, STB
	Gp		: Cumulative gas produced, scf
	Wp		: Cumulative water produced, bbl

	Rp		: Cumulative gas-oil ratio, scf/STB
	
	Ginj	: Cumulative gas injected, scf
	Winj	: Cumulative water injected, STB

	We		: Cumulative water influx, bbl

	"""

	Np 		: float = 0.
	Gp 		: float = 0.
	Wp 		: float = 0.

	Ginj 	: float = 0.
	Winj 	: float = 0.

	We 		: float = 0.

	@property
	def Rp(self):
		return numpy.nan if self.Np==0 else self.Gp/self.Np
	
