from dataclasses import dataclass

@dataclass
class ResProp:
	"""RESERVOIR ROCK & FLUID PROPERTY CALCULATION METHODS

	Bo		: Oil formation volume factor, bbl/STB
	Bw 		: Water formation volume factor, bbl/STB
	Bg		: Gas formation volume factor, bbl/scf

	cw		: Water compressibility, psi−1
	cf		: Formation (rock) compressibility, psi−1

	Rs		: Gas solubility, scf/STB

	Pb		: Bubble point pressure, psi

	"""

	Pb 		: float = None