import numpy as np

#  Create a matrix of 4 X 3 with Numbers 0 to 11
mat = np.arange(12).reshape(4,3)
print(mat)

#  Create a matrix of 4 X 3 with Numbers 0 to 11
mult = mat * 3
print(mult)

#  Create a matrix Transpose of mat
transp = mat.T
print(transp)

# Broadcasting 15 to all the first 2 rows of mat
mat[:3,:3] = 15
print(mat)

# 'all', 'any', 'argmax', 'argmin', 'argpartition', 'argsort', 'astype', 'base', 'byteswap', 'choose', 'clip', 'compress', 'conj', 'conjugate', 
# 'copy', 'ctypes', 'cumprod', 'cumsum', 'data', 'diagonal', 'dot', 'dtype', 'dump', 'dumps', 'fill', 'flags', 'flat', 'flatten', 'getfield', 
# 'imag', 'item', 'itemset', 'itemsize', 'max', 'mean', 'min', 'nbytes', 'ndim', 'newbyteorder', 'nonzero', 'partition', 'prod', 'ptp', 'put', 
# 'ravel', 'real', 'repeat', 'reshape', 'resize', 'round', 'searchsorted', 'setfield', 'setflags', 'shape', 'size', 'sort', 'squeeze', 'std', 'strides', 'sum', 
# 'swapaxes', 'take', 'tobytes', 'tofile', 'tolist', 'tostring', 'trace', 'transpose', 'var', 'view'
print(dir(mat))
