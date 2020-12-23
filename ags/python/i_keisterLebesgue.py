>>> def my_L_Keister(x): # create a custom function
...    d = x.shape[1]
...    norm_sq = (x**2).sum(1)
...    out = np.cos(np.sqrt(norm_sq))*np.exp(-norm_sq)
...    return out  # size n vector
>>> lebesgue = qp.Lebesgue(qp.Halton(2), lower_bound = -inf, upper_bound = inf) # define Lebesgue measure based on Halton
>>> keister = qp.CustomFun(lebesgue, my_L_Keister) # define transformed integrand
>>> y = keister.f(keister.distribution.gen_samples(1000)) # evaluate transformed integrand at Halton points
>>> y.mean() # approximate the integral
1.8121845342791671