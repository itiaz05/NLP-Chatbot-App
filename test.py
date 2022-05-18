from torch import device
import torch
import torch.nn as nn
from model import create_data_loader

def test_model(X,Y, model):
    #Hyperparameters:
    learning_rate = 0.01

    data_loader = create_data_loader(X, Y)
    
    # Compute Loss and use Optimizier 
    criterion = nn.CrossEntropyLoss() # to calc the entropy loss between input and target
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate) # Adam optimizier alg, to update network weights iterative based in training data

    for (words,labels) in data_loader:
        words = words.to(device)
        labels = labels.to(dtype=torch.long).to(device)

        # Forward
        outputsVectors = model(words)
        loss = criterion(outputsVectors, labels) 

        # Send Loss Backwards
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        print(f'final loss loss={loss.item():.4f}') 