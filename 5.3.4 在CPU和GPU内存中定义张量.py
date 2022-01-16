import torch

# 将CPU内存的张量复制到GPU内存中
a = torch.FloatTensor([4])
b = a.cuda()
print(b)

# 直接在GPU内存中定义张量
a = torch.tensor([4], device='cuda')
print(a)

# 使用to()方法指定设备
a = torch.FloatTensor([4])
print(a)
print(a.to('cuda:0'))

# 使用环境变量
import os
os.environ['CUDA_VISIBLE_DEVICES'] = "0"
