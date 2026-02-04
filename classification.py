"""
text classification using bert model
"""

import torch 
import torch.nn as nn
import torch.nn.functional as F
from typing import Optional, Tuple
import math
import numpy as np
import argparse

class BertModel(nn.Module):
    def __init__(self, config):
        super().__init__()

    def forward(
        self,
        input_ids: torch.LongTensor,
        token_type_ids: Optional[torch.LongTensor] = None,
        position_ids: Optional[torch.LongTensor] = None,
    ):
        return 


if __name__ == "__main__":
    print("text classification using bert model")
    np.random.seed(1)
    torch.manual_seed(1)

    # dataset config
    dataset = "THUCNews"
    
    # model config
    model = BertModel()


    # model training
    

    # model evaling