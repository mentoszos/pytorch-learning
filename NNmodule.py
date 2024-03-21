import torch
import torch.nn.functional as F
inputt = torch.tensor([[1, 2, 0, 3, 1],
                       [0, 1, 2, 3, 1],
                       [1, 2, 1, 0, 0],
                       [5, 2, 3, 1, 1],  # 注意这里应该是 5 列，而不是 4 列
                       [2, 1, 0, 1, 1]])
kernel = torch.tensor([[1, 2, 1],
                       [0, 1, 0],
                       [2, 1, 0]])

inputt = torch.reshape(inputt,(1,1,5,5))
kernel = torch.reshape(kernel,(1,1,3,3))
outputt = F.conv2d(inputt,kernel,stride=1)
print(outputt)