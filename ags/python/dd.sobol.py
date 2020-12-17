>>> sobol = qp.Sobol(2,randomize=False)
>>> sobol.gen_samples(8,warn=False)
array([[0.   , 0.   ],
       [0.5  , 0.5  ],
       [0.25 , 0.75 ],
       [0.75 , 0.25 ],
       [0.125, 0.625],
       [0.625, 0.125],
       [0.375, 0.375],
       [0.875, 0.875]])