import numpy as np
from torch import device
import torch
from torch.utils.data import DataLoader
from neuralNet import NeuralNet
import torch.nn as nn
from DataSet import DataSet
from model import create_data_loader


def train_model(X,Y, model):
    #Hyperparameters:
    learning_rate = 0.01
    num_epochs = 100

    data_loader = create_data_loader(X, Y)

    # Loss and Optimizer
    criterion = nn.CrossEntropyLoss() # to calc the entropy loss between input and target
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate) # Adam optimizier alg, to update network weights iterative based in training data
    for epoch in range(num_epochs):
        for (words,labels) in data_loader:
            words = words.to(device)
            labels = labels.to(dtype=torch.long).to(device)

            # Forward
            outputsVectors = model(words)
            loss = criterion(outputsVectors, labels) 

            # Backward and Optimizer step
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
    
        if (epoch + 1) % 1 == 0:
            print(f'epoch {epoch+1}/{num_epochs},loss={loss.item():.4f}')

    print(f'final loss loss={loss.item():.4f}')
    return model

