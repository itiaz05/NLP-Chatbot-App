import torch.nn as nn

class NeuralNet(nn.Module):
    def __init__(self,input_size,hidden_size,num_classes):
        super(NeuralNet,self).__init__()
        self.inputLayer = nn.Linear(input_size,hidden_size) # First hidden layer in the NeuralNet
        self.hiddenLayer = nn.Linear(hidden_size,hidden_size) # Second hidden layer in the NeuralNet
        self.classesLayer = nn.Linear(hidden_size,num_classes) # The Third is the output of number classes
        self.relu = nn.ReLU(); # Accelerates convergence


    def forward(self,x):
        out = self.inputLayer(x)
        out = self.relu(out)
 
        out = self.hiddenLayer(out)
        out = self.relu(out)

        out = self.classesLayer(out)
        
        # No activiation and no SoftMax
        return out
