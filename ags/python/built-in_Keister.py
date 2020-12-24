>>> keister = qp.Keister(qp.Gaussian(qp.Halton(2), mean = 0, covariance = 1/2))
>>> keister.f(keister.distribution.gen_samples(1000)).mean() # approximate integral
1.8058776436618529
>>> keister = qp.Keister(qp.Lebesgue(qp.Halton(2), lower_bound = -np.inf, upper_bound = np.inf))
>>> keister.f(keister.distribution.gen_samples(1000)).mean() # approximate integral
1.8027010141523265