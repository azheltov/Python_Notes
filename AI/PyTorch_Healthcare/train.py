import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import DataLoader, Dataset
import pandas as pd
from PIL import Image
import os

# 1. Load CSV metadata file here.. it has image names and stuff 
class ChestXrayDataset(Dataset):
    def __init__(self, csv_file, img_dir, transform=None, disease='Pneumonia'):
        self.data = pd.read_csv(csv_file)  # load csv with image metadata
        self.img_dir = img_dir  # where my images are stored
        self.transform = transform  # optional transforms
        self.disease = disease  # target disease

        # setting up binary labels, 1 if 'pneumonia', else 0
        self.data[self.disease] = self.data['Finding Labels'].apply(lambda x: 1 if disease in x else 0)

    def __len__(self):
        return len(self.data)  # return total images in dataset

    def __getitem__(self, idx):
        # get image path and label
        img_name = os.path.join(self.img_dir, self.data.iloc[idx, 0])  # the image path
        image = Image.open(img_name).convert('RGB')  # load the image

        # get the label (1 or 0)
        label = torch.tensor(self.data.iloc[idx][self.disease], dtype=torch.long)

        if self.transform:
            image = self.transform(image)  # apply any transformation

        return image, label  # return image and label for training

# 2. Transforms to resize images and normalize
transform = transforms.Compose([
    transforms.Resize((128, 128)),  # resize all images to same size
    transforms.ToTensor(),  # convert to PyTorch tensor
    transforms.Normalize((0.5,), (0.5,))  # normalize so the data is more balanced
])

# 3. Create dataset loader for training
train_data = ChestXrayDataset(csv_file='path/to/your/metadata.csv', img_dir='path/to/images', transform=transform)
train_loader = DataLoader(train_data, batch_size=32, shuffle=True)  # shuffling so not in same order

# 4. Simple CNN for pneumonia detection (nothing fancy yet)
class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 32, kernel_size=3, padding=1)  # first convolution layer, 3-channel (RGB)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)  # second conv layer, more filters
        self.fc1 = nn.Linear(64 * 32 * 32, 128)  # fully connected layer after flattening
        self.fc2 = nn.Linear(128, 2)  # final layer for binary output (Pneumonia or Not)

    def forward(self, x):
        x = torch.relu(self.conv1(x))  # activation function after 1st conv
        x = torch.max_pool2d(x, 2)  # max pooling to reduce size
        x = torch.relu(self.conv2(x))  # activation after 2nd conv
        x = torch.max_pool2d(x, 2)  # max pooling again
        x = x.view(-1, 64 * 32 * 32)  # flatten the image for FC layer
        x = torch.relu(self.fc1(x))  # pass through fully connected layer
        x = self.fc2(x)  # final layer, no activation here, output will be logits
        return x

# 5. Training setup
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')  # use GPU if available
model = SimpleCNN().to(device)  # send model to device
criterion = nn.CrossEntropyLoss()  # loss function for classification
optimizer = optim.Adam(model.parameters(), lr=0.001)  # Adam optimizer, learning rate set

# 6. Training Loop (small number of epochs for now)
n_epochs = 5
for epoch in range(n_epochs):
    model.train()  # set model to training mode
    running_loss = 0.0  # track the loss for each epoch
    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)  # send data to GPU/CPU
        optimizer.zero_grad()  # clear previous gradients
        outputs = model(images)  # forward pass
        loss = criterion(outputs, labels)  # calculate loss
        loss.backward()  # backpropagate
        optimizer.step()  # update weights
        running_loss += loss.item()  # keep track of loss
    print(f"Epoch [{epoch+1}/{n_epochs}], Loss: {running_loss/len(train_loader):.4f}")  # print epoch loss

# 7. Save the Model
torch.save(model.state_dict(), 'pneumonia_cnn.pth')  # save trained model weights

# 8. (Optional) Test the model on new unseen data
# Load a few test images and make predictions (future step)
