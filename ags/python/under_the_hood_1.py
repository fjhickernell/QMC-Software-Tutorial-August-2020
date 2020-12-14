from qmcpy import *
bm = BrownianMotion(Lattice(16))
ao = AsianOption(bm,
    call_put = 'call',
    start_price = 30,
    strike_price = 35)
sc = CubQMCLatticeG(ao, abs_tol=1e-4)
sol,data = sc.integrate()