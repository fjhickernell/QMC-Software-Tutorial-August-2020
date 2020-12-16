>>> g = qp.Gaussian(qp.Sobol(2,seed=7), 
        mean = [3.,2.], 
        covariance = [[9.,5.], [5.,4.]])
>>> g.gen_samples(n_min=4,n_max=8)
array([[3.424, 0.708],
       [4.541, 3.896],
       [0.412, 0.636],
       [9.339, 5.329]])