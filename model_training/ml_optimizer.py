import torch
from ml_loss import *
from ml_tools import *
from ml_generate import *

class Optimizer():
    def __init__(self, model,
                 op, # Adam, SGD, RMSprop
                 weight_decay,
                 learning_rate,
                 device,
                 conserve_lepton_number
                 ): 
        self.NF = model.NF
        self.optimizer = op(model.parameters(), weight_decay=weight_decay, lr=learning_rate)
        self.device = device
        self.conserve_lepton_number = conserve_lepton_number

class AsymptoticOptimizer(Optimizer):
    # function to train the dataset
    def train(self, model, F4i, F4f_true, loss_fn):
        model.train()
        F4f_pred = model.predict_F4(F4i, conserve_lepton_number=self.conserve_lepton_number)
        loss = loss_fn(model, F4f_pred, F4f_true)
        return loss

    # function to test the model performance
    def test(self, model, F4i, F4f_true, loss_fn):
        model.eval()
        with torch.no_grad():
            F4f_pred = model.predict_F4(F4i, conserve_lepton_number=self.conserve_lepton_number)
            loss = loss_fn(model, F4f_pred, F4f_true)
            if F4f_true != None:
                error = torch.max(torch.abs(F4f_pred - F4f_true))
            else:
                error = None
            return loss, error
            
class StabilityOptimizer(Optimizer):
    # function to train the dataset
    # note that the loss function MUST be BCEWithLogitsLoss
    # Because of this, y is NOT wrapped by sigmoid
    def train(self, model, F4i, unstable, loss_fn):
        model.train()
        X = model.X_from_F4(F4i)
        y = model.forward(X)
        loss = loss_fn(y, unstable)
        return loss
    
    # function to test the model performance
    # note that the loss function MUST be BCEWithLogitsLoss
    # Because of this, y is NOT wrapped by sigmoid
    def test(self, model, F4i, unstable, loss_fn):
        model.eval()
        with torch.no_grad():
            X = model.X_from_F4(F4i)
            y = model.forward(X)
            loss = loss_fn(y, unstable)
            error = torch.max(torch.abs(torch.sigmoid(y) - unstable))
            return loss, error