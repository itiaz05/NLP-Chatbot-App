import json
import spacy
import numpy as np
from torch import device
import torch
from torch.utils.data import DataLoader
from neuralNet import NeuralNet
from preProcess import clean_pattern,bag_of_words
from DataSet import DataSet
from sklearn.model_selection import train_test_split
from test import test_model
from train import train_model

# Samples - A sample is a single row of data. It contains inputs that are fed into the algorithm and an output that
#           is used to compare to the prediction and calculate an error.
#
# Batch - The batch size is a hyperparameter that defines the number of samples
#         to work through before updating the internal model parameters.


# Input: data as tuples of (sentence : tag) 
# Output: return X data and Y data as numppy array
def build_data(dataTuples):
    X_data = []
    Y_data = []
    for (pattern_sentence,tag) in dataTuples:
        bag = bag_of_words(pattern_sentence,all_words)
        X_data.append(bag)
        labels = tags.index(tag) # Get index of each tag
        Y_data.append(labels) 
    return np.array(X_data), np.array(Y_data)

# Input: X = data , Y = tags/labels
# Output: Data Loader (to use in train|test funcs)
def create_data_loader(X, Y):
    # Hyperparameters
    batch_size = 8 
    data = DataSet(X, Y) # Save our data
    return DataLoader(dataset=data,batch_size=batch_size,shuffle=True,num_workers=0)

nlp = spacy.load("en_core_web_lg")

with open('intents.json','r') as file:
    intents = json.load(file)

all_words = [] # store here for bag of words (the X-training data) 
tags = [] # store here all the tags for classification (this is the Y-training data)
xy = [] # Tuples of (sentence : tag)

# Read the json and do some pre processing Clean
for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag)
    for pattern in intent['patterns']:
        sentence_tokenize = clean_pattern(pattern)
        all_words.extend(sentence_tokenize)
        xy.append((sentence_tokenize,tag))

# Remove duplicate words to and sort
all_words = sorted(dict.fromkeys(all_words))
tags = sorted(dict.fromkeys(tags)) 

training_data, test_data = train_test_split(xy, test_size = 0.2, random_state = 25, shuffle=True)

# X Store bag of words, Y Store labels (tags)
X_train, Y_train = build_data(training_data) 
X_test, Y_test = build_data(test_data) 

# Hyperparameters
hidden_size_nn = 8
output_size_nn = len(tags)
input_size = len(X_train[0])

# Check if we have GPU support
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

model = NeuralNet(input_size, hidden_size_nn,output_size_nn).to(device)

train_data_loader = create_data_loader(X_train, Y_train)
test_data_loader = create_data_loader(X_train, Y_train)

train_model(model,train_data_loader,device)
test_model(model,test_data_loader,device) # want to return something or just print the prob?

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