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
print(torch.tensor([1, 3].dtype))

