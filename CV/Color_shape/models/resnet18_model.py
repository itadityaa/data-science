import torch
import torch.nn as nn
import torchvision.models as models

class ResNetModel(nn.Module):
    def __init__(self, num_classes):
        super(ResNetModel, self).__init__()
        
        # Load a pre-trained ResNet model
        self.resnet = models.resnet18(pretrained=True)
        
        # Replace the final fully connected layer to output the correct number of classes
        self.resnet.fc = nn.Linear(self.resnet.fc.in_features, num_classes)
        
    def forward(self, x):
        return self.resnet(x)
