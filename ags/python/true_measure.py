from qmcpy import Lattice, Gaussian
l = Lattice(dimension=2)
gl = Gaussian(l, mean=0, covariance=1/2)
xg = gl.gen_samples(2**7)