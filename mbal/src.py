"""

Pi 		: Initial reservoir pressure, psi
P 		: Volumetric average reservoir pressure
Dp 		: Change in reservoir pressure = Pi−P, psi
Pb		: Bubble point pressure, psi
N 		: Initial (original) oil in place, STB
Np 		: Cumulative oil produced, STB
Gp		: Cumulative gas produced, scf
Wp		: Cumulative water produced, bbl
Rp		: Cumulative gas-oil ratio, scf/STB
GOR		: Instantaneous gas-oil ratio, scf/STB
Rsi		: Initial gas solubility, scf/STB
Rs		: Gas solubility, scf/STB
Boi		: Initial oil formation volume factor, bbl/STB
Bo		: Oil formation volume factor, bbl/STB
Bgi		: Initial gas formation volume factor, bbl/scf
Bg		: Gas formation volume factor, bbl/scf
Bt 		: Two-phase formation volume factor
Winj	: Cumulative water injected, STB
Ginj	: Cumulative gas injected, scf
We		: Cumulative water influx, bbl
M 		: Ratio of initial gas-cap-gas reservoir volume to initial reservoir oil volume, bbl/bbl
G		: Initial gas-cap gas, scf
PV		: Pore volume, bbl
cw		: Water compressibility, psi−1
cf		: Formation (rock) compressibility, psi−1

"""

def get_M(G,Bgi,N,Bgi):
	return G*Bgi/(N*Boi)

def get_PV(N,Boi,M,Swi):
	return N*Boi*(1+M)/(1-Swi)

def get_Bt(Bo,Rsi,Rs,Bg):
	return Bo+(Rsi-Rs)*Bg

def get_A(Np,Bt,Rp,Rsi,Bg):
	return Np*(Bt+(Rp-Rsi)*Bg)

def get_DDI(N,Bt,Bti,A):
	return N*(Bt-Bti)/A

def get_SDI(N,M,Bti,Bg,Bgi,A):
	return N*M*Bti*(Bg-Bgi)/(A*Bgi)