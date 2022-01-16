import torch

# 统计元素个数
a = torch.Tensor(2)
print(torch.numel(a))

# 张量的判断
print(torch.is_tensor(a))

# 张量的类型转换
a = torch.FloatTensor([4])
print(a.type(torch.IntTensor))
print(a.type(torch.DoubleTensor))
print(a.int())
print(a.double())

# 重载操作符函数
a = torch.FloatTensor([4])
print(a)
b = torch.add(a, a)
print(b)

# 自变化运算函数
a.add_(b)
print(a)

# 数学运算函数
print(a.mean())
print(a.sqrt())

# 张量与numpy之间的相互转换
import numpy as np
a = torch.FloatTensor([5])
print(a.numpy())
anp = np.asarray([4])
print(torch.from_numpy(anp))
print(torch.tensor(anp))

# 张量与numpy各自形状的获取
x = torch.rand(1, 2)
y = torch.randn(1, 2)
print(x.shape, x.size())
print(y.shape, y.size())
anp = np.asarray([1, 2])
print(anp.shape, anp.size)

# 张量与numpy各自的切片操作
print(x[:])
print(anp[:])
print(anp[anp > 0.5])
