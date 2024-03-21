import torch
from torch import nn
from torch.nn import Conv2d, MaxPool2d, Flatten, Linear
from torch.utils.tensorboard import SummaryWriter


class Tudui(nn.Module):
    def __init__(self):
        super(Tudui, self).__init__()

        self.model1 = nn.Sequential(Conv2d(3,32,5,padding="same"),MaxPool2d(2),Conv2d(32,32,5,padding="same"),MaxPool2d(2),Conv2d(32,64,5,padding="same"),MaxPool2d(2),
                                    Flatten(),Linear(1024,64),Linear(64, 10))

    def forward(self,x):
        x = self.model1(x)
        return x

tudui  = Tudui()
print(tudui)
inputt = torch.ones((64,3,32,32))
outputt = tudui(inputt)
print(outputt.shape)
writer = SummaryWriter("logs_seq")
writer.add_graph(tudui,inputt)
writer.close()