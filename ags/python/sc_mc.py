>>> # MC problem
>> dd_mc = qp.IIDStdGaussian(dimension=2,seed=7)
>>> m_mc = qp.Gaussian(dd_mc,mean=0.,covariance=1./2)
>>> i_mc = qp.Keister(m_mc)
>>> sc_mc = qp.CubMCG(i_mc,abs_tol=1e-3)
>>> solution_mc,data_mc = sc_mc.integrate()
>>> print(data_mc)
Solution: 1.8085         
Keister (Integrand Object)
IIDStdGaussian (DiscreteDistribution Object)
    dimension       2^(1)
    seed            7
    mimics          StdGaussian
Gaussian (TrueMeasure Object)
    mean            0
    covariance      2^(-1)
    decomp_type     pca
CubMCG (StoppingCriterion Object)
    inflate         1.200
    alpha           0.010
    abs_tol         0.001
    rel_tol         0
    n_init          2^(10)
    n_max           10000000000
MeanVarData (AccumulateData Object)
    levels          1
    solution        1.809
    n               14448691
    n_total         14449715
    error_bound     1.00e-03
    confid_int      [1.808 1.81 ]
    time_integrate  2.378