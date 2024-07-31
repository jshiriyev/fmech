from ._state import State

from ._reservoir import Reservoir

from ._dynamic import Dynamic

class MBTank(State):

	def __init__(self,state:dict=None,reservoir:dict=None,dynamic:dict=None):
		"""Initialization of Material Balance Tank Model."""

		if state is None:
			super().__init__()
		else:
			super().__init__(**state)

		self._res = Reservoir() if reservoir is None else Reservoir(**reservoir)

		self._dyn = Dynamic() if dynamic is None else Dynamic(**dynamic)

	@property
	def res(self):
		return self._res

	@property
	def dyn(self):
		return self._dyn

	@property
	def M(self):
		"""Ratio of gas-cap-gas reservoir volume to
		reservoir oil volume, bbl/bbl"""
		return self.G*self.res.Bg/(self.N*self.res.Bo)

	@property
	def PV(self):
		"""Pore volume, bbl"""
		return self.N*self.res.Bo*(1+self.M)/(1-self.Sw)