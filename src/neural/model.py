import torch
import torch.nn as nn

class OthelloTransformerEval(nn.Module):
    """
    Transformer model for board evaluation .
    Uses multi-head attention to capture long-range dependencies.[10, 11]
    """
    def __init__(self, embed_dim=128, num_heads=8):
        super().__init__()
        self.embedding = nn.Linear(1, embed_dim)
        self.encoder = nn.MultiheadAttention(embed_dim, num_heads, batch_first=True)
        self.fc = nn.Sequential(
            nn.Linear(embed_dim * 64, 256),
            nn.ReLU(),
            nn.Linear(256, 1)
        )

    def forward(self, x):
        # x: [batch, 64]
        x = x.unsqueeze(-1).float()
        x = self.embedding(x)
        attn_out, _ = self.encoder(x, x, x)
        out = attn_out.reshape(x.size(0), -1)
        return self.fc(out)