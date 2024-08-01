import copy

from ._reservoir import Reservoir

from ._phase import Phase

from ._operation import Operation

class Model():

	def __init__(self,**kwargs):
		"""Initialization of Material Balance Tank Model."""

		self._reservoir = Reservoir(**Reservoir.get(**kwargs))

		self._phase = Phase(**Phase.get(**kwargs))

		self._operation = Operation(**Operation.get(**kwargs))

	def __call__(self,**kwargs):
		"""Updating altered Material Balance Tank Model properties."""

		new = copy.deepcopy(self)

		for key,value in kwargs.items():

			if key in self.reservoir.__dict__:
				setattr(new.reservoir,key,value)
			elif key in self.phase.__dict__:
				setattr(new.phase,key,value)
			elif key in self.operation.__dict__:
				setattr(new.operation,key,value)
			else:
				print(f"Warning: Key '{key}' not found in any sub-class properties.")

		return new

	@property
	def reservoir(self):
		return self._reservoir

	@property
	def phase(self):
		return self._phase

	@property
	def operation(self):
		return self._operation

	@property
	def gcg2oil(self):
		"""Ratio of gas-cap-gas reservoir volume to reservoir oil volume, bbl/bbl"""
		return (self.reservoir.G*self.phase.Bg)/(self.reservoir.N*self.phase.Bo)

	@property
	def porevolume(self):
		"""Pore volume, bbl"""
		return (self.reservoir.N*self.phase.Bo)*(1+self.gcg2oil)/(1-self.reservoir.Sw)