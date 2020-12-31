>>> lattice = qp.Lattice(dimension=2,randomize=False)
>>> lattice.gen_samples(n=8)
warnings.warn("Non-randomized lattice sequence includes the origin",ParameterWarning)
array([[0.   , 0.   ],
       [0.5  , 0.5  ],
       [0.25 , 0.75 ],
       [0.75 , 0.25 ],
       [0.125, 0.875],
       [0.625, 0.375],
       [0.375, 0.625],
       [0.875, 0.125]])