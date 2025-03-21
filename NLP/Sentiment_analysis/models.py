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
class BiLSTMSentiment(nn.Module):
    def __init__(self, embedding_dim=50, hidden_dim=128):
        super().__init__()
        self.lstm = nn.LSTM(embedding_dim, hidden_dim, bidirectional=True, batch_first=True)
        self.fc = nn.Linear(hidden_dim * 2, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        _, (hidden, _) = self.lstm(x)
        hidden = torch.cat((hidden[-2,:,:], hidden[-1,:,:]), dim=1)  # Combine bidirectional states
        return self.sigmoid(self.fc(hidden))
class CNNTextClassifier(nn.Module):
    def __init__(self, embedding_dim=50, num_filters=100):
        super().__init__()
        self.conv = nn.Conv1d(embedding_dim, num_filters, kernel_size=3, padding=1)
        self.fc = nn.Linear(num_filters, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = x.permute(0, 2, 1)  # Reshape to (batch, embedding_dim, sequence_length)
        x = torch.relu(self.conv(x))
        x = torch.max(x, dim=2)[0]  # Global Max Pooling
        return self.sigmoid(self.fc(x))