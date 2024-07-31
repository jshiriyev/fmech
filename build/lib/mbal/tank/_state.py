from dataclasses import dataclass

@dataclass
class State:
	"""VOLUMETRIC AVERAGE PARAMETERS FOR MATERIAL BALANCE TANK

	P 		: Volumetric average reservoir pressure
			  at which fluid and rock properties are defined, psi

	Sw 		: Water saturation,

	N 		: Oil in place, STB
	G		: Gas-cap gas, scf

	GOR		: Instantaneous gas-oil ratio, scf/STB

	"""

	P 		: float = None
	Sw 		: float = None

	N 		: float = None
	G 		: float = None

	GOR 	: float = None