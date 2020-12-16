>>> sobol = qp.Sobol(4) # t = [1/4, 1/2, 3/4, 1]
>>> aco = qp.AsianOption(
...         qp.BrownianMotion(sobol, drift=2), 
...         start_price = 30,
...         strike_price = 45,
...         volatility = 0.5,
...         interest_rate = 0,
...         call_put = 'call')
>>> x = sobol.gen_samples(2**10)
>>> y = aco.f(x)
>>> y.mean()
0.4349545319177899