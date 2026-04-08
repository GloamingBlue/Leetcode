import torch
import torch.nn as nn
import torch.nn.functional as F


class Linear(nn.Module):  # 专家网络
    def __init__(self, in_features: int, out_features: int) -> None:
        super(Linear, self).__init__()
        self.fc = nn.Linear(in_features, out_features)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.fc(x)
    

class MoELayer(nn.Module):
    def __init__(self, num_experts: int, in_features: int, out_features: int) -> None:
        super(MoELayer, self).__init__()
        self.num_experts = num_experts
        self.experts = nn.ModuleList([Linear(in_features, out_features) for _ in range(self.num_experts)])
        self.gate = nn.Linear(in_features, self.num_experts)  # 门控

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        gate_score = F.softmax(self.gate(x), dim=-1)
        expert_outputs = torch.stack([expert(x) for expert in self.experts], dim=1)  # 在维度1上堆叠：(batch_size,num_experts,out_features)
        output = torch.bmm(gate_score.unsqueeze(1), expert_outputs).squeeze(1)  # (batch_size,1,num_experts) @ (batch_size,num_experts,out_features) = (batch_size,1,out_features), squeeze(1)后为(batch_size,out_features)
        return output


if __name__ == '__main__':
    input_size = 5
    output_size = 3
    num_experts = 4
    batch_size = 10
    model = MoELayer(num_experts, input_size, output_size)
    demo = torch.randn(batch_size, input_size)
    output = model(demo)
    print(output, output.shape)
