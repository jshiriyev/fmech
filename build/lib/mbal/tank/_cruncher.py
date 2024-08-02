from ._model import Model

class Cruncher:

	@staticmethod
	def M(model0:Model):
		"""Ratio of gas-cap-gas reservoir volume to reservoir oil volume, bbl/bbl"""
		return (model0.reservoir.G*model0.phase.Bg)/(model0.reservoir.N*model0.phase.Bo)

	@staticmethod
	def PV(model0:Model):
		"""Total pore volume, bbl"""
		return (model0.reservoir.N*model0.phase.Bo)*(1+Cruncher.M(model0))/(1-model0.reservoir.Sw)

	@staticmethod
	def Btotal(model0:Model,model:Model):
		"""Two-phase formation volume factor"""
		return model.phase.Bo+(model0.phase.Rs-model.phase.Rs)*model.phase.Bg

	@staticmethod
	def Ntotal(model0:Model,model:Model):
		"""Two-phase total production"""
		return model.operation.Np*(Cruncher.Btotal(model0,model)+(model.operation.Rp-model0.phase.Rs)*model.phase.Bg)

	@staticmethod
	def DDI(model0:Model,model:Model):
		"""Depletion drive index"""
		return model0.reservoir.N*(Cruncher.Btotal(model0,model)-model0.phase.Bo)/Cruncher.Ntotal(model0,model)

	@staticmethod
	def SDI(model0:Model,model:Model):
		"""Segregation (gas-cap) drive index"""
		return model0.reservoir.N*Cruncher.M(model0)*model0.phase.Bo*(model.phase.Bg-model0.phase.Bg)/(model0.phase.Bg*Cruncher.Ntotal(model0,model))

	@staticmethod
	def WDI(model0:Model,model:Model):
		"""Water drive index"""
		return (model.reservoir.We-model.operation.Wp*model.phase.Bw)/Cruncher.Ntotal(model0,model)

	@staticmethod
	def EDI(model0:Model,model:Model):
		"""Expansion (rock and liquid) depletion drive"""
		return Cruncher.PV(model0)*(model.phase.cf+model.phase.cw*model0.reservoir.Sw)*(model0.reservoir.P-model.reservoir.P)/Cruncher.Ntotal(model0,model)