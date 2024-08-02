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

	def optimize(tank,index,**kwargs):

		for key,value in kwargs.items():
			break

		def objective(value,key,index):

			tank[index] = tank[index](**{key:value[0].tolist()})

			tank[index].reservoir.G = 0.2*value[0].tolist()*tank[index].phase.Bo/tank[index].phase.Bg

			return (tank.DDI[1]+tank.SDI[1]+tank.WDI[1]-1)**2

		sol = minimize(objective,value,args=(key,index),tol=1e-5,method="Powell")

		# if sol.success:
		# 	setattr(tank.original,key,sol.x[0])
	    
		return tank	# tank = optimize(tank,0,N=1000_000)

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
