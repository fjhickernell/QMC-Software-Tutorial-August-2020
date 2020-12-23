>>> def my_Keister(x): # create a custom function
...	d = x.shape[1]
...     norm = np.sqrt((x**2).sum(1)) # sum along rows
...     out = np.pi**(d/2)*np.cos(norm)
...     return out  # size n vector
>>> gaussian = qp.Gaussian(qp.Halton(d), mean = 0, covariance = 1/2) # define a Gaussian measure based on Halton
>>> keister = qp.CustomFun(gaussian, custom_fun=my_Keister) # define transformed integrand
>>> y = keister.f(cf.distribution.gen_samples(1000)) # evaluate transformed integrand at Halton points
>>> y.mean() # approximate the integral by the sample mean
1.8070543509894346
