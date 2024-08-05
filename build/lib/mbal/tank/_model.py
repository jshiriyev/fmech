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

	def __call__(self,inplace=False,**kwargs):
		"""Updating Material Balance Tank Model properties."""

		if not inplace:
			self = copy.deepcopy(self)

		for key,value in kwargs.items():

			if key in self.reservoir.__dict__:
				setattr(self.reservoir,key,value)
			elif key in self.phase.__dict__:
				setattr(self.phase,key,value)
			elif key in self.operation.__dict__:
				setattr(self.operation,key,value)
			else:
				print(f"Warning: Key '{key}' not found in any sub-class properties.")

		if not inplace:
			return self

	@property
	def reservoir(self):
		return self._reservoir

	@property
	def phase(self):
		return self._phase

	@property
	def operation(self):
		return self._operation