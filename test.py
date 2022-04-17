import torch


x = torch.Tensor([1,2,3,4])

y = torch.Tensor([1,2,3,1])


z = torch.concat((x,y))

print(y+x/2)
print(z) 