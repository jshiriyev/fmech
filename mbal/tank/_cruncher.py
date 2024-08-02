from ._model import Model

class Cruncher:

	@staticmethod
	def M(initial:Model):
		"""Ratio of gas-cap-gas reservoir volume to reservoir oil volume, bbl/bbl"""
		return (initial.reservoir.G*initial.phase.Bg)/(initial.reservoir.N*initial.phase.Bo)

	@staticmethod
	def PV(initial:Model):
		"""Total pore volume, bbl"""
		return (initial.reservoir.N*initial.phase.Bo)*(1+Cruncher.M(initial))/(1-initial.reservoir.Sw)

	@staticmethod
	def Btotal(initial:Model,model:Model):
		"""Two-phase formation volume factor"""
		return model.phase.Bo+(initial.phase.Rs-model.phase.Rs)*model.phase.Bg

	@staticmethod
	def Ntotal(initial:Model,model:Model):
		"""Two-phase total production"""
		return model.operation.Np*(Cruncher.Btotal(initial,model)+(model.operation.Rp-initial.phase.Rs)*model.phase.Bg)

	@staticmethod
	def DDI(initial:Model,model:Model):
		"""Depletion drive index"""
		return initial.reservoir.N*(Cruncher.Btotal(initial,model)-initial.phase.Bo)/Cruncher.Ntotal(initial,model)

	@staticmethod
	def SDI(initial:Model,model:Model):
		"""Segregation (gas-cap) drive index"""
		return initial.reservoir.N*Cruncher.M(initial)*initial.phase.Bo*(model.phase.Bg-initial.phase.Bg)/(initial.phase.Bg*Cruncher.Ntotal(initial,model))

	@staticmethod
	def WDI(initial:Model,model:Model):
		"""Water drive index"""
		return (model.reservoir.We-model.operation.Wp*model.phase.Bw)/Cruncher.Ntotal(initial,model)

	@staticmethod
	def EDI(initial:Model,model:Model):
		"""Expansion (rock and liquid) depletion drive"""
		return Cruncher.PV(initial)*(model.phase.cf+model.phase.cw*initial.reservoir.Sw)*(initial.reservoir.P-model.reservoir.P)/Cruncher.Ntotal(initial,model)