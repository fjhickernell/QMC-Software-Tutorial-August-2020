>>> bm = qp.BrownianMotion(qp.Sobol(4), drift=2)
>>> bm.gen_samples(2)
array([[ 1.017,  1.503,  2.205,  4.085],
       [ 0.174,  0.117,  0.107, -0.089]])