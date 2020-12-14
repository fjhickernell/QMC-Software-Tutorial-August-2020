from qmcpy import Sobol
s = Sobol(dimension=2)
x = s.gen_samples(2**10)