>>> sobol = qp.Sobol(2,randomize=False)
>>> sobol.gen_samples(n_min=4,n_max=8,warn=False)
array([[0.25 , 0.75 ],
       [0.75 , 0.25 ],
       [0.125, 0.625],
       [0.625, 0.125],
       [0.375, 0.375],
       [0.875, 0.875]])