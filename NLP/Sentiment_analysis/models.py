import torch
import torch.nn as nn

# Define LSTM Model
class LSTMModel(nn.Module):
    def __init__(self, embedding_dim=50, hidden_dim=128, output_dim=1):
        super().__init__()
        self.lstm = nn.LSTM(embedding_dim, hidden_dim, batch_first=True)
        self.fc = nn.Linear(hidden_dim, output_dim)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        _, (hidden, _) = self.lstm(x)  # Extract last hidden state
        out = self.fc(hidden[-1])  # Fully connected layer
        return self.sigmoid(out)