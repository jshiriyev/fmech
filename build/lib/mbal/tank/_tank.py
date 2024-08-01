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
