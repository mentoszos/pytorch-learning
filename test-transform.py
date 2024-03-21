from PIL import Image
from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms

img_path = "D:\\pytorch-learning\\hymenoptera_data\\train\\ants\\0013035.jpg"
img_Image = Image.open(img_path)
img_Image.show()
trans_tensor = transforms.ToTensor()
img_tensor = trans_tensor(img_Image)
writer = SummaryWriter("logs")
writer.add_image("test",img_tensor)
writer.close()
