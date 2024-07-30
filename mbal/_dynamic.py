from dataclasses import dataclass

@dataclass
class Dynamic:
	"""PRODUCTION-INJECTION-INFLUX PARAMETERS

	Id  	: step index at which all the parameters below are defined,

	Np 		: Cumulative oil produced, STB
	Gp		: Cumulative gas produced, scf
	Wp		: Cumulative water produced, bbl

	Rp		: Cumulative gas-oil ratio, scf/STB
	
	Ginj	: Cumulative gas injected, scf
	Winj	: Cumulative water injected, STB

	We		: Cumulative water influx, bbl

	"""

	Id  	: int = None

	Np 		: float = None
	Gp 		: float = None
	Wp 		: float = None

	Ginj 	: float = 0.
	Winj 	: float = 0.

	We 		: float = None

	@property
	def Rp(self):
		return self.Gp/self.Np
	
