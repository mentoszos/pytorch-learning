from torch.utils.data import Dataset
from PIL import Image
import os
class MyData(Dataset):
    def __init__(self,root_dir,label_dir):
        self.root_path = root_dir
        self.label_dir = label_dir
        self.path =os.path.join(root_dir, label_dir)
        self.img_path = os.listdir(self.path)

    def __getitem__(self, idx):
        img_name = self.img_path[idx]
        img_path = os.path.join(self.root_path, self.label_dir, img_name)
        img = Image.open(img_path)
        label = self.label_dir
        return img, label

    def __len__(self):
        return len(self.img_path)

root_dir = "D:\\pytorch-learning\\hymenoptera_data\\train"
label_dir = "ants"
ant_dataset = MyData(root_dir,label_dir)
img, label = ant_dataset[0]
img.show()
