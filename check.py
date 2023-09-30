# 检查pytorch版本
import torch 
print(torch.__version__)
print(torch.cuda.is_available())

# 检查是否使用cuda
device = torch.device("cuda:0" if (torch.cuda.is_available()) else "cpu")
print(device)
print(torch.cuda.get_device_name(0))