>>> l = qp.Lattice(2)
>>> gl = qp.Gaussian(l, mean=0, covariance=1/2)
>>> gl.gen_samples(n_min=4, n_max=8)
array([[ 0.238, -0.559],
       [-0.791,  0.401],
       [ 0.836,  1.279],
       [-0.213, -0.063]])