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

	step 	: time step at which all the parameters above are defined,

	"""

	Np 		: float = None
	Gp 		: float = None
	Wp 		: float = None

	Ginj 	: float = 0.
	Winj 	: float = 0.

	step 	: float = None

	@property
	def Rp(self):
		return self.Gp/self.Np
	
