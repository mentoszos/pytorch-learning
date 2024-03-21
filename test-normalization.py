from PIL import Image
from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms
writer = SummaryWriter("logs")
img = Image.open("D:\\pytorch-learning\\练手数据集\\train\\ants_image\\5650366_e22b7e1065.jpg")
trans_tensor = transforms.ToTensor()
img_tensor = trans_tensor(img)
writer.add_image("totensor",img_tensor)
print(img_tensor[0][0][0])
trans_norm = transforms.Normalize([0.5,0.5,0.5],[0.5,0.5,0.5])
img_norm = trans_norm(img_tensor)
writer.add_image("norm",img_norm)
transforms.RandomCrop()
print(img_norm[0][0][0])
