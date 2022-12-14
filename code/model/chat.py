import json
import torch
import spacy
from neuralNet import NeuralNet
from preProcess import bag_of_words,clean_pattern
from afterProcess import create_patterns,getNumbers

nlp = spacy.load("en_core_web_lg")

with open('code\model\intents.json','r') as file:
    intents = json.load(file)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Load the data file that contain dictionary of hyperparameters 
FILE_PATH = "code\server\model\dataFile.pth"
data = torch.load(FILE_PATH)

THRESHOLD = 0.75

# Params to our model
input_size = data["input_size"] 
output_size = data["output_size"] 
hidden_size = data["hidden_size"] 
all_words = data["all_words"] 
model_state = data["model_state"] 
tags = data["tags"] 

model = NeuralNet(input_size, hidden_size,output_size).to(device)

# Copy all the learned params (model state) and buffer into our model and evaluate him
model.load_state_dict(model_state)
model.eval()

# The func create_patterns() return Matcher obj after insert our patterns to matcher
matcher = create_patterns()

bot_name = "Amdocs"
print(f"\n{bot_name}: Welcome, how can i help you? (for exit type quit)")

def get_response(msg):
    sentence = clean_pattern(msg)
    bagOfWords = bag_of_words(sentence,all_words)
    bagAfterReshape = bagOfWords.reshape(1,bagOfWords.shape[0]) # Gives 1 row because we have 1 sample and [0] because our model 
    bagAsNumpyArray = torch.from_numpy(bagAfterReshape).to(device)

    outputVector = model(bagAsNumpyArray)
    _, predicatedVector = torch.max(outputVector,dim=1)
    
    tag = tags[predicatedVector.item()]
    
    # Use to extraxt the number with the matcher
    sentenceAsDoc = nlp(" ".join(sentence))
    match = matcher(sentenceAsDoc)
    dictOfIdentifiers = getNumbers(match,sentenceAsDoc)

    softmax = torch.softmax(outputVector,dim=1) # use softmax regression on the output because we use multi classes
    probability = softmax[0][predicatedVector.item()]
    # print(probability.item())

    if probability.item() > THRESHOLD:
        for intent in intents["intents"]:
            if tag == intent["tag"]:
                intentReponse = intent["response"]
                print(f"{bot_name}: {intentReponse}")
    else:
        print(f"{bot_name}: sorry i dont understand you...")
