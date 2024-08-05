import numpy

from scipy.optimize import minimize

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

	def minimize(self,drive_index=None,alter_initial=False,minimize_dict:dict=None,**kwargs):
		"""
		Minimizes the difference between total drive index and 1 for the given drive_index model.

		drive_index 	: the model index that is used to calculate total drive index.

		alter_initial 	: the model index whose parameters will be altered.

		Returns the OptimizeResult where the x includes the optimized values of kwargs keys.
		"""

		prime_model = self[0]()

		drive_model = self[-1]() if drive_index is None else self[drive_index]()

		keys,values = list(kwargs.keys()),list(kwargs.values())

		def objective(values,keys):

			if alter_initial:
				prime_model = prime_model(**dict(zip(keys,values)))
			else:
				drive_model = drive_model(**dict(zip(keys,values)))

			# prime_model.reservoir.G = 0.2*value[0].tolist()*prime_model.phase.Bo/prime_model.phase.Bg

			ddi = self.safe_drive_index(prime_model,drive_model,"DDI")
			sdi = self.safe_drive_index(prime_model,drive_model,"SDI")
			wdi = self.safe_drive_index(prime_model,drive_model,"WDI")
			edi = self.safe_drive_index(prime_model,drive_model,"EDI")

			return (ddi+sdi+wdi+edi-1)**2

		return minimize(objective,values,args=(keys,),**minimize_dict) # minimize(tank,0,N=1000_000)

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

	@staticmethod
	def safe_drive_index(initial,model,method="DDI"):
		"""Safely calculates the drive index, if error, returns 0"""
		try:
			return getattr(Cruncher,method)(initial,model)
		except:
			return 0

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
