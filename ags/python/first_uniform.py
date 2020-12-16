>>> u = qp.Uniform(qp.Sobol(2), lower_bound=[-2,0], upper_bound=[2,4])
>>> u.gen_samples(4)
array([[ 1.376,  3.205],
       [-1.812,  1.872],
       [ 0.203,  0.835],
       [-0.608,  2.245]])