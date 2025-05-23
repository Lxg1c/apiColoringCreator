import torch

print("CUDA доступна:", torch.cuda.is_available())
if torch.cuda.is_available():
    print("Устройство:", torch.cuda.get_device_name(0))
    print("Версия CUDA:", torch.version.cuda)
else:
    print("CUDA не активна, проверь установку.")
