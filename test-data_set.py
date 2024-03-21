import torchvision
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter


writer = SummaryWriter("dataloader")
data_transforms = torchvision.transforms.Compose([
    torchvision.transforms.ToTensor()
])
# train_set = torchvision.datasets.CIFAR10(root="./dataset", train=True, download=True,transform=data_transforms)
test_set = torchvision.datasets.CIFAR10(root="./testset",train=False,download=False,transform=data_transforms)
test_loader = DataLoader(test_set,4,True,num_workers=0,drop_last=False)
step = 1;
for data in test_loader:
    imgs,targets = data
    writer.add_images("testloader",imgs,global_step=step)
    step = step+1

writer.close()

