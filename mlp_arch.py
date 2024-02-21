import torch 
from torch import nn 

class MLP_image(nn.Module):
    
    def __init__(self):
        super().__init__()
        self.seq = nn.Sequential(
            nn.Linear(1000, 10),
            nn.ReLU(), 
            nn.Linear(10, 50), 
            nn.ReLU(), 
            nn.Linear(50, 1), 
            nn.Sigmoid()
        )        
    
    
    def forward(self, x: torch.Tensor):
        x = x.flatten()
        return self.seq(x)
