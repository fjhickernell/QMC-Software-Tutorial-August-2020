>>> u = qp.Uniform(qp.Halton(2), 
            lower_bound = [-2,0], 
            upper_bound = [2,4])
>>> u.gen_samples(4)
array([[ 0.85908285,  0.85683196],
       [-1.14091715,  2.19016529],
       [ 1.85908285,  3.52349863],
       [-0.14091715,  1.30127641]])