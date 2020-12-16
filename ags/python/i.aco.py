>>> dd = qp.Sobol(4,seed=7)
>>> m = qp.BrownianMotion(dd)
>>> ac = qp.AsianOption(m)
>>> x = dd.gen_samples(2**10)
>>> y = ac.f(x)
>>> y.mean()
FIX CODE with start price, strike price, call option, ...