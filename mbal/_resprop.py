from dataclasses import dataclass

@dataclass
class ResProp:
	"""RESERVOIR ROCK & FLUID PARAMETERS

	P 		: Volumetric average reservoir pressure
			  at which below parameters are defined, psi

	Bo		: Oil formation volume factor, bbl/STB
	Bw 		: Water formation volume factor, bbl/STB
	Bg		: Gas formation volume factor, bbl/scf

	cw		: Water compressibility, psi−1
	cf		: Formation (rock) compressibility, psi−1

	Pb		: Bubble point pressure, psi

	Rs		: Gas solubility, scf/STB

	GOR		: Instantaneous gas-oil ratio, scf/STB

	N 		: Oil in place, STB
	G		: Gas-cap gas, scf

	Sw 		: Water saturation,

	We		: Cumulative water influx, bbl

	"""

	P 		: float = None

	Bo 		: float = 1.
	Bw 		: float = 1.
	Bg		: float = None

	cw 		: float = 1e-6
	cf 		: float = 1e-6

	Pb 		: float = None

	Rs 		: float = None

	GOR 	: float = None

	N 		: float = None
	G 		: float = None

	Sw 		: float = None

	We 		: float = None

	@property
	def M(self):
		"""Ratio of gas-cap-gas reservoir volume to
		reservoir oil volume, bbl/bbl"""
		return self.G*self.Bg/(self.N*self.Bo)

	@property
	def PV(self):
		"""Pore volume, bbl"""
		return self.N*self.Bo*(1+self.M)/(1-self.Sw)