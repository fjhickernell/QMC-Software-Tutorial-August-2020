>>> sobol = qp.Sobol(2,randomize=False)
>>> sobol.gen_samples(8)
/usr/local/lib/python3.6/dist-packages/qmcpy/discrete_distribution/sobol/sobol.py:180: ParameterWarning: Non-randomized AGS Sobol sequence includes the origin
  warnings.warn("Non-randomized AGS Sobol sequence includes the origin",ParameterWarning)
array([[0.   , 0.   ],
       [0.5  , 0.5  ],
       [0.25 , 0.75 ],
       [0.75 , 0.25 ],
       [0.125, 0.625],
       [0.625, 0.125],
       [0.375, 0.375],
       [0.875, 0.875]])