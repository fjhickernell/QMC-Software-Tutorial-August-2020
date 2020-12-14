from qmcpy import Sobol, Gaussian, Keister, CubQMCSobolG
k = Keister(Gaussian(Sobol(3),covariance=1/2))
sc = CubQMCSobolG(k, abs_tol=1e-4)
solution,data = sc.integrate()