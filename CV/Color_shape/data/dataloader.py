import os
import torch
import pandas as pd
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms
from PIL import Image
from sklearn.preprocessing import MultiLabelBinarizer

class ShapeColorDataset(Dataset):
    def __init__(self, csv_file, root_dir, transform=None):
        """
        Args:
            csv_file (str): Path to the CSV file with image paths & labels.
            root_dir (str): Directory containing images.
            transform (callable, optional): Transformations to apply to images.
        """
        self.data = pd.read_csv(csv_file)
        self.root_dir = root_dir
        self.transform = transform
        
        self.data['label'] = self.data['label'].apply(self.clean_labels)
        
        self.mlb = MultiLabelBinarizer()
        self.encoded_labels = self.mlb.fit_transform(self.data['label'])
        
        self.classes = self.mlb.classes_

    def clean_labels(self, label_str):
        """
        Clean up the label string (remove unwanted characters like '(' and ')').
        """
        label_str = label_str.strip("[]").replace("'", "").replace("(", "").replace(")", "")
        return label_str.split(", ")

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        img_path = os.path.join(self.root_dir, self.data.iloc[idx, 0])
        image = Image.open(img_path).convert("RGB")
        
        if self.transform:
            image = self.transform(image)

        # Convert labels to multi-hot encoding
        label = torch.tensor(self.encoded_labels[idx], dtype=torch.float32)

        return image, label

# Define transformations
default_transform = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
])

def get_dataloader(csv_file, root_dir, batch_size=32, shuffle=True, num_workers=2):
    dataset = ShapeColorDataset(csv_file, root_dir, transform=default_transform)
    return DataLoader(dataset, batch_size=batch_size, shuffle=shuffle, num_workers=num_workers), dataset.classes
