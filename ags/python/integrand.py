from qmcpy import Halton, CustomFun, Gaussian
import numpy as np
# create a custom function
d = 3
def my_Keister(x):
    norm = np.sqrt((x**2).sum(1))
    k = np.cos(norm)*np.exp(-norm**2)
    return k  # size n vector
# define QMCPy components
lebesgue = Lebesgue(Halton(d), lower_bound=-np.inf, upper_bound=np.inf)
fv = CustomFun(lebesgue, custom_fun=my_Keister)

# Use QMCPy objects to evaluate integrand
x = cf.distribution.gen_samples(2**7) # generate Halton samples
y = cf.f(x) # evaluate transformed integrand at Halton points
y.mean() # approximate the mean of the distribution 