"""
text classification
"""

import torch 
import torch.nn as nn
import torch.nn.functional as F
from typing import Optional, Tuple
import math


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
    print("hello")