>>> lattice = qp.Lattice(dimension=2,randomize=False)
>>> lattice.gen_samples(n=8)
/usr/local/lib/python3.6/dist-packages/qmcpy/discrete_distribution/lattice/lattice.py:197: ParameterWarning: Non-randomized lattice sequence includes the origin
  warnings.warn("Non-randomized lattice sequence includes the origin",ParameterWarning)
array([[0.   , 0.   ],
       [0.5  , 0.5  ],
       [0.25 , 0.75 ],
       [0.75 , 0.25 ],
       [0.125, 0.875],
       [0.625, 0.375],
       [0.375, 0.625],
       [0.875, 0.125]])