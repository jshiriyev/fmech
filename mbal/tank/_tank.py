import numpy

from ._model import Model

from ._cruncher import Cruncher

class Tank(list):

	def __init__(self,**kwargs):

		super().__init__((Model(**kwargs),))

	def append(self,**kwargs):

		super().append(self[-1](**kwargs))

	def extend(self,iterable):

		if not all(isinstance(item,Model) for item in iterable):
			raise TypeError("All items in the iterable must be Model instances")

		super().extend(iterable)

	def insert(self,index,**kwargs):

		if index==0:
			raise IndexError("Insert cannot initialize the tank.")

		super().insert(index,self[index-1](**kwargs))

	@property
	def original(self):
		return self[0]
	
	@property
	def M(self):
		"""Ratio of gas-cap-gas reservoir volume to reservoir oil volume, bbl/bbl"""
		return Cruncher.M(self.original)

	@property
	def PV(self):
		"""Total pore volume, bbl"""
		return Cruncher.PV(self.original)
	
	@property
	def DDI(self):
		"""Depletion drive index"""
		return [Cruncher.DDI(self.original,model) for model in self]

	@property
	def SDI(self):
		"""Segregation (gas-cap) drive index"""
		return [Cruncher.SDI(self.original,model) for model in self]

	@property
	def WDI(self):
		"""Water drive index"""
		return [Cruncher.WDI(self.original,model) for model in self]

	@property
	def EDI(self):
		"""Expansion (rock and liquid) depletion drive"""
		return [Cruncher.EDI(self.original,model) for model in self]
