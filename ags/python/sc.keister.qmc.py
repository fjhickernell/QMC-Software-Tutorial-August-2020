>>> # QMC problem
>>> dd_qmc = qp.Sobol(dimension=2,seed=7)
>>> m_qmc = qp.Gaussian(dd_qmc,mean=0.,covariance=1./2)
>>> i_qmc = qp.Keister(m_qmc)
>>> sc_qmc = qp.CubQMCSobolG(i_qmc,abs_tol=1e-3)
>>> solution_qmc,data_qmc = sc_qmc.integrate()
>>> print(data_qmc)
Solution: 1.8081         
Keister (Integrand Object)
Sobol (DiscreteDistribution Object)
    dimension       2^(1)
    randomize       1
    graycode        0
    seed            [61616 58565]
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
    solution        1.808
    error_bound     5.01e-04
    time_integrate  0.013