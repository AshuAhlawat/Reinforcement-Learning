import torch

x = torch.tensor((1.0,2,3,4))

y = torch.tensor((5,6,7))

z = x.std()
print(z)