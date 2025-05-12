import torch

print("CUDA доступен:", torch.cuda.is_available())

print("Количество устройств CUDA:", torch.cuda.device_count())

print("Имя устройства 0:", torch.cuda.get_device_name(0))

x = torch.rand(3, 3).to('cuda')
print("Тензор на GPU:", x)

# Обучение модели на GPU (1 эпоха)
model = torch.nn.Linear(10, 1).to('cuda')
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
loss_fn = torch.nn.MSELoss()

inputs = torch.randn(5, 10).to('cuda')
targets = torch.randn(5, 1).to('cuda')

optimizer.zero_grad()
outputs = model(inputs)
loss = loss_fn(outputs, targets)
loss.backward()
optimizer.step()

print("Один шаг обучения на GPU выполнен успешно!")
