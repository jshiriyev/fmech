import copy

from ._reservoir import Reservoir

from ._phase import Phase

from ._operation import Operation

class Model():

	def __init__(self,gcgperoil=None,porevolume=None,**kwargs):
		"""Initialization of Material Balance Tank Model."""

		self._gcgperoil  = gcgperoil
		self._porevolume = porevolume

		self._reservoir  = Reservoir(**Reservoir.get(**kwargs))

		self._phase      = Phase(**Phase.get(**kwargs))

		self._operation  = Operation(**Operation.get(**kwargs))

		self.calculate_missing_property()

	@property
	def reservoir(self):
		return self._reservoir

	@property
	def phase(self):
		return self._phase

	@property
	def operation(self):
		return self._operation

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

	def calculate_missing_property(self):

		if self.phase.Bo is None or self.phase.Bg is None:
			return

		if self.reservoir.N is not None and self.reservoir.G is not None:
			self._gcgperoil  = (self.reservoir.G*self.phase.Bg)/(self.reservoir.N*self.phase.Bo)
		elif self.reservoir.N is not None and self._gcgperoil is not None:
			self.reservoir.G = (self.reservoir.N*self.phase.Bo)*self._gcgperoil/self.phase.Bg
		elif self.reservoir.G is not None and self._gcgperoil is not None:
			self.reservoir.N = (self.reservoir.G*self.phase.Bg)/(self._gcgperoil*self.phase.Bo)

	@property
	def N(self):
		return self.reservoir.N
	
	@N.setter
	def N(self,value):
		self.reservoir.N = value
		self.calculate_missing_property()

	@property
	def G(self):
		return self.reservoir.G

	@G.setter
	def G(self,value):
		self.reservoir.G = value
		self.calculate_missing_property()

	@property
	def gcgperoil(self):
		return self._gcgperoil

	@gcgperoil.setter
	def gcgperoil(self,value):
		self._gcgperoil = value
		self.calculate_missing_property()

	@property
	def porevolume(self):
		return self._porevolume
	