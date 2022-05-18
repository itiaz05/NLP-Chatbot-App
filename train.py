import torch
import torch.nn as nn

def train_model(model, data_loader,device):
    #Hyperparameters:
    learning_rate = 0.01
    num_epochs = 100

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

