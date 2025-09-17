import numpy as np
a=np.matrix([[1,2,3,23],
             [4,5,6,25],
             [7,8,9,28],
             [10,11,12,41]])
print("the rank is:", np.linalg.matrix_rank(a))
