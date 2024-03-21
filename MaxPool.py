import torch
from torch import nn


class Tudui(nn.Module):
    def __init__(self):
        super(Tudui, self).__init__()
        self.maxpool1 = nn.MaxPool2d(3,ceil_mode=True)

    def forward(self,x):
        return self.maxpool1(x)


iput = torch.tensor([[1,2,0,3,1],
                     [0,1,2,3,1],
                     [1,2,1,0,0],
                     [5,2,3,1,1],
                     [2,1,0,1,1]])
iput = torch.reshape(iput,(-1,1,5,5))
tudui = Tudui()
outputt = tudui(iput)
print(outputt)

