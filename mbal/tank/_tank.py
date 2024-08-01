from ._model import Model

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
	def DDI(self):
		"""depletion drive index"""
		return self.reso.N*(self.Bt-self.reso.Bo)/self.A

	@property
	def SDI(self):
		"""segregation (gas-cap) drive index"""
		return self.reso.N*self.reso.M*self.reso.Bo*self.DBg/(self.reso.Bg*self.A)

	@property
	def WDI(self):
		"""water drive index"""
		return (self.res.We-self.dyn.Wp*self.res.Bw)/self.A

	@property
	def EDI(self):
		"""expansion (rock and liquid) depletion drive"""
		return self.reso.N*self.reso.Bo*(1+self.reso.M)*self.BP*self.Dp/self.A
