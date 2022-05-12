import json
import spacy
import numpy as np
from torch import device
import torch
from torch.utils.data import DataLoader
from model import NeuralNet
import torch.nn as nn
from preProcess import bag_of_words_TF_IDF, clean_pattern,bag_of_words
from DataSet import DataSet
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

# Samples - A sample is a single row of data. It contains inputs that are fed into the algorithm and an output that
#           is used to compare to the prediction and calculate an error.
#
# Batch - The batch size is a hyperparameter that defines the number of samples
#         to work through before updating the internal model parameters.

def build_data(dataTuples):
    X_data = []
    Y_data = []
    for (pattern_sentence,tag) in dataTuples:
        bag = bag_of_words(pattern_sentence,all_words)
        X_data.append(bag)
        labels = tags.index(tag) # Get index of each tag
        Y_data.append(labels) 
    return X_data, Y_data

# Input: X = data , Y = tags/labels
def create_data_loader(X, Y):
    # Hyperparameters
    batch_size = 8 

    data = DataSet(X, Y) # Save our data
    return DataLoader(dataset=data,batch_size=batch_size,shuffle=True,num_workers=0)

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

def test_model(X,Y, model):
    #Hyperparameters:
    num_epochs = 100
    learning_rate = 0.01

    data_loader = create_data_loader(X, Y)
    
    # Compute Loss 
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

nlp = spacy.load("en_core_web_lg")

with open('intents.json','r') as file:
    intents = json.load(file)

all_words = [] # store here for bag of words (the X-training data) 
tags = [] # store here all the tags for classification (this is the Y-training data)
xy = [] # Tuples of (sentence : tag)
xy_test = [] # Tuples to test (sentence : tag)

# Read the json and do some pre processing Clean
for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag)
    for pattern in intent['patterns']:
        sentence_tokenize = clean_pattern(pattern)
        all_words.extend(sentence_tokenize)
        xy.append((sentence_tokenize,tag))

training_data, test_data = train_test_split(xy, test_size = 0.2, random_state = 25, shuffle=True)

# Remove duplicate words to and sort
all_words = sorted(dict.fromkeys(all_words))
tags = sorted(dict.fromkeys(tags)) 

X_train, Y_train = build_data(training_data) # X_train Store bag of words, Y_train Store labels (tags)
X_test, Y_test = build_data(test_data) # X_train Store bag of words, Y_train Store labels (tags)

# Hyperparameters
hidden_size_nn = 8
output_size_nn = len(tags)
input_size = len(X_train[0])


# Check if we have GPU support
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

model = NeuralNet(input_size, hidden_size_nn,output_size_nn).to(device)

model = train_model(X_train, Y_train, model)
test_model(X_test, Y_test, model)

# Save/Load the model and implement the chat 
data = {
    "model_state": model.state_dict(),
    "input_size": input_size,
    "output_size": output_size_nn,
    "hidden_size": hidden_size_nn,
    "all_words": all_words,
    "tags": tags,
}

# Save our model in pyTorch file
FILE_PATH = "C:\MyProjects\AmdocsProject\dataFile.pth"
torch.save(data,FILE_PATH)

print(f'Training Complete!\nfile saved to {FILE_PATH}')