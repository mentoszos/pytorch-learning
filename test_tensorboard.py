from torch.utils.tensorboard import SummaryWriter
from PIL import Image
import numpy as np
writer = SummaryWriter("logs")
img_PIL = Image.open("练手数据集/train/ants_image/0013035.jpg")
img_np = np.array(img_PIL)
print(img_np.shape)
writer.add_image("test",img_np,global_step=1,dataformats="HWC")


writer.close()
