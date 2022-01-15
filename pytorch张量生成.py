import torch
import numpy as np

# 将已有数值转换为张量
a = torch.tensor(5)
print(a)
anp = np.asarray([4])
a = torch.tensor(anp)
print(a)

# 数据类型
print(torch.get_default_dtype())
print(torch.tensor([4, 5]).dtype)
torch.set_default_dtype(torch.float64)
print(torch.get_default_dtype())
print(torch.tensor([1, 3]).dtype)

# 指定形状的张量
a = torch.Tensor(2)
print(a)
b = torch.Tensor(1, 2)
print(b)
c = torch.empty(1, 2)
print(c)
# 指定内容的张量
c = torch.Tensor([2])
print(c)
d = torch.Tensor([1, 2])
print(d)
# 指定形状、指定内容的张量
a = torch.zeros(1, 3)
print(a)
a = torch.ones(1, 3)
print(a)
a = torch.ones_like(a)
print(a)
c = torch.randn(1, 4)
print(c)
d = torch.eye(4, 4)
print(d)
e = torch.full(size=(5, 4), fill_value=1)
print(e)

# 设置随机种子
torch.manual_seed(2)
print(torch.initial_seed())

# 线性、对数空间的随机值
print(torch.arange(1, 10, step=3))
print(torch.linspace(1, 9, steps=5))
print(torch.logspace(1, 9, steps=5))
