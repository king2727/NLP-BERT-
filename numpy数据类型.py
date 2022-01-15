import numpy as np

# 对角矩阵
v = np.array([1, 8, 4])
print(np.diag(v))

# 单位矩阵
print(np.eye(3))

# hadamard Product
a = np.array(range(4)).reshape(2, 2)
b = np.array(range(4, 8)).reshape(2, 2)
print(a*b)

# Dot Product
print(a@b)
print(np.dot(a, b))
ma = np.asmatrix(a)
mb = np.asmatrix(b)
print(ma*mb)

# 对角矩阵与向量的互转
a = np.diag([1, 2, 3])
print(a)
v, e = np.linalg.eig(a)
print(v, e)

# 对角矩阵幂运算
print(a*a*a)
print(a@a@a)
print(a**3)

# 求矩阵的逆
print(np.linalg.inv(a))
A = np.asmatrix(a)
print(A.I)
print(A.I@a)

# 矩阵相乘
a = np.diag([1, 2, 3])
b = np.ones([3, 3])
print(a@b)
print(b@a)