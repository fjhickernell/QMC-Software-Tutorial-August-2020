>>> keister = qp.Keister(qp.Gaussian(qp.Sobol(2),covariance=1./2))
>>> stopping = qp.CubQMCSobolG(keister,abs_tol=1e-3)
>>> solution_qmc,data_qmc = stopping.integrate()
>>> print(data_qmc)
Solution: 1.8086         
Keister (Integrand Object)
Sobol (DiscreteDistribution Object)
    dimension       2^(1)
    randomize       1
    graycode        0
    seed            [91844 20561]
    mimics          StdUniform
    dim0            0
Gaussian (TrueMeasure Object)
    mean            0
    covariance      2^(-1)
    decomp_type     pca
CubQMCSobolG (StoppingCriterion Object)
    abs_tol         0.001
    rel_tol         0
    n_init          2^(10)
    n_max           2^(35)
LDTransformData (AccumulateData Object)
    n_total         2^(13)
    solution        1.809
    error_bound     6.17e-04
    time_integrate  0.016