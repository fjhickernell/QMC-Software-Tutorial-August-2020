>>> import numpy as np
d = 2 # dimension
>>> def my_Keister(x): # create a custom function
...     norm = np.sqrt((x**2).sum(1))
...     k = np.pi**(d/2)*np.cos(norm)
...     return k  # size n vector
>>> # define QMCPy components
>>> lebesgue = qp.Gaussian(qp.Halton(d), mean=0, covariance=1/2)
>>> cf = qp.CustomFun(lebesgue, custom_fun=my_Keister)
>>> 
>>> # Use QMCPy objects to evaluate integrand
>>> x = cf.distribution.gen_samples(2**7) # generate Halton samples
>>> y = cf.f(x) # evaluate transformed integrand at Halton points
>>> y.mean() # approximate the mean of the distribution
1.808723467976591
