import numpy as np
from scipy import sparse

#1と0の対角行列

eye = np.eye(4)
print("NumPy arrey\n{}".format(eye))

#NumPy配列をSciPyのCSR形式の疎行列に変換する（？？？）
#0でないものが格納される
sparse_matrix = sparse.csr_matrix(eye)
print("\nScrPy sparate CSR matrix\n{}".format(sparse_matrix))

print("\n")

#another(COO形式) 検索=>scipy Lecture Notes
data = np.ones(4)
row_indices = np.arange(4)
col_indices = np.arange(4)
eye_coo = sparse.coo_matrix((data,(row_indices, col_indices)))

print("COO representation\n{}".format(eye_coo))
