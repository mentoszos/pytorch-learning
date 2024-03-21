import torch
import torchvision
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter


class Tudui(torch.nn.Module):
    def __init__(self):
        super(Tudui, self).__init__()
        self.conv1 = torch.nn.Conv2d(in_channels=3, out_channels=6, kernel_size=3, stride=1, padding=0)

    def forward(self, x):
        x = self.conv1(x)
        return x


dataset = torchvision.datasets.CIFAR10("testset", False, transform=torchvision.transforms.ToTensor())
dataloader = torch.utils.data.DataLoader(dataset, 64)

tudui = Tudui()
writer = SummaryWriter("logs")
step = 0
for data in dataloader:
    imgs, targets = data
    writer.add_images("original", imgs, global_step=step)
    outputt = tudui(imgs)
    outputt = torch.reshape(outputt,(-1,3,30,30))
    writer.add_images("changed", outputt, global_step=step)
    step = step + 1
    print(step)
