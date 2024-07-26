from _resprop import ResProp
from _dynamic import Dynamic

class Solver():

	def __init__(self,**kwargs):
		"""resoialization of the solver"""
		self.reso = ResProp(**kwargs)

	def __call__(self,res:ResProp,dyn:Dynamic):

		self.res = res
		self.dyn = dyn

		return self

	@property
	def Bt(self):
		"""Total (two-phase) formation volume factor"""
		return self.res.Bo+(self.reso.Rs-self.res.Rs)*self.res.Bg

	@property
	def A(self):
		"""Empirical parameter defined for the simplicity"""
		return self.dyn.Np*(self.Bt+(self.dyn.Rp-self.reso.Rs)*self.res.Bg)

	@property
	def BP(self):
		return (self.res.cf+self.res.cw*self.reso.Sw)/(1-self.reso.Sw)
	
	@property
	def Dp(self):
		"""Change in reservoir pressure"""
		return self.reso.P-self.res.P

	@property
	def DBg(self):
		return self.res.Bg-self.reso.Bg

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

	@property
	def CUM(self):
		"""cumulative of drive indices"""
		return self.DDI+self.SDI+self.WDI+self.EDI
		
if __name__ == "__main__":

	Pi = 3000

	Boi = 1.58
	Bwi = 1.0
	Bgi = 0.00080

	Rsi = 1040

	Ni = 10_000_000
	Gi = 0.25*(10_000_000*1.58)/0.00080

	Swi = 0.2

	sol = Solver(P=Pi,Bo=Boi,Bw=Bwi,Bg=Bgi,Rs=Rsi,N=Ni,G=Gi,Sw=Swi)

	print(sol.reso.M)

	res = ResProp(P=2800,Bo=1.48,Rs=850,Bg=0.00092,Bw=1.0,cw=1.5e-6,cf=1e-6)

	dyn = Dynamic(Np=1_000_000,Gp=1_100_000_000,Wp=50_000)

	print(dyn.Rp)

	sol1 = sol(res,dyn)

	wdi = 1-sol1.DDI-sol1.SDI-sol1.EDI

	We = wdi*sol1.A+dyn.Wp*res.Bw

	print(We)

	print(sol1.A)

	print(sol1.DDI)
	print(sol1.SDI)
	print(wdi)
	print(sol1.EDI)
