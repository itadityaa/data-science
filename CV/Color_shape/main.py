import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import warnings
warnings.filterwarnings("ignore")

from data.dataloader import get_dataloader
from models.cnn_model import SimpleCNN
from models.resnet18_model import ResNetModel

# Early Stopping Callback
class EarlyStopping:
    def __init__(self, patience=5, delta=0.001, save_path="C:/Users/itadi/Desktop/data-science/CV/Color_shape/saved_models/initial_model.pth"):
        self.patience = patience
        self.delta = delta
        self.save_path = save_path
        self.best_loss = float('inf')
        self.counter = 0

    def check(self, val_loss, model):
        if val_loss < self.best_loss - self.delta:
            self.best_loss = val_loss
            self.counter = 0
            torch.save(model.state_dict(), self.save_path)
            print(f"Model Saved (Best Loss: {val_loss:.4f})")
        else:
            self.counter += 1
            print(f"Early Stopping Counter: {self.counter}/{self.patience}")

        return self.counter >= self.patience  # Stop if patience exceeded

if __name__ == "__main__":
    csv_path = "C:/Users/itadi/Desktop/data-science/CV/Color_shape/data/raw/train.csv"
    image_dir = "C:/Users/itadi/Desktop/data-science/CV/Color_shape/data/raw"

    print("\nLoading Data...")
    dataloader, class_names = get_dataloader(csv_path, image_dir, batch_size=32)
    num_classes = len(class_names)
    print(f"Data Loaded! Number of Classes: {num_classes}\n")

    # Model selection
    model = SimpleCNN(num_classes=num_classes)
    # model = ResNetModel(num_classes=num_classes)  # Uncomment to use ResNet

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = model.to(device)

    print(f"Using device: {device}")

    criterion = nn.BCEWithLogitsLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer, mode='min', factor=0.5, patience=3, verbose=True)

    early_stopping = EarlyStopping(patience=5)

    epochs = 20
    print("\nStarting Training...\n")

    for epoch in range(epochs):
        model.train()
        running_loss = 0.0
        correct, total = 0, 0

        progress_bar = tqdm(dataloader, desc=f"Epoch {epoch+1}/{epochs}", leave=True)
        for images, labels in progress_bar:
            images, labels = images.to(device), labels.to(device)

            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item()

            preds = torch.sigmoid(outputs) > 0.5
            correct += (preds == labels).sum().item()
            total += labels.numel()

            progress_bar.set_postfix(loss=loss.item())

        epoch_loss = running_loss / len(dataloader)
        accuracy = 100 * correct / total
        scheduler.step(epoch_loss)  

        print(f"Epoch {epoch+1} - Loss: {epoch_loss:.4f} | Accuracy: {accuracy:.2f}%")

        # Early stopping check
        if early_stopping.check(epoch_loss, model):
            print("\nTraining Stopped Early!")
            break

    print("\nTraining Completed!")