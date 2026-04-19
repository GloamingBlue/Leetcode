import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import Optional


class GQA(nn.Module):  # MHA本质上和GQA差距不大，没有了num_kv_heads也就不需要kv的repeat了  # 这里省去了对qk的旋转位置编码还有kv cache的实现
    def __init__(self, hidden_size: int, head_dim: int, num_heads: int, num_kv_heads: int) -> None:
        super(GQA, self).__init__()
        assert num_heads % num_kv_heads == 0
        self.head_dim = head_dim
        self.num_heads = num_heads
        self.num_kv_heads = num_kv_heads
        self.group_size = num_heads // num_kv_heads

        self.q_proj = nn.Linear(hidden_size, self.num_heads * self.head_dim)
        self.k_proj = nn.Linear(hidden_size, self.num_kv_heads * self.head_dim)
        self.v_proj = nn.Linear(hidden_size, self.num_kv_heads * self.head_dim)
        self.o_proj = nn.Linear(self.num_heads * self.head_dim, hidden_size)

    def forward(self, x: torch.Tensor, mask: Optional[torch.Tensor]=None) -> torch.Tensor:
        B, S, _ = x.shape
        # 投影+拆分
        q = self.q_proj(x).view(B, S, self.num_heads, self.head_dim)
        k = self.k_proj(x).view(B, S, self.num_kv_heads, self.head_dim)
        v = self.v_proj(x).view(B, S, self.num_kv_heads, self.head_dim)
        # 重复kv
        k = k.repeat_interleave(self.group_size, dim=2)
        v = v.repeat_interleave(self.group_size, dim=2)
        # 转置S和H的维度，方便进行多头注意力的计算
        q = q.transpose(1, 2)
        k = k.transpose(1, 2)
        v = v.transpose(1, 2)
        # 计算注意力得分
        scores = q @ k.transpose(-2, -1) / math.sqrt(self.head_dim)
        if mask is not None:  # mask为因果掩码，上三角为全0，不包含主对角线
            scores = scores.masked_fill(mask == 0, float('-inf'))
        attn = F.softmax(scores, dim=-1)
        # 计算加权的注意力
        out = attn @ v
        out = out.transpose(1, 2).contiguous().view(B, S, -1)
        return self.o_proj(out)
