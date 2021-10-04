import torch
import torchvision.models as models
import numpy as np
import matplotlib.pyplot as plt
from pthflops import count_ops
from timeit import default_timer as timer

# device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
device = torch.device('cpu')
print("device: ", device)

#model = models.resnet18(pretrained=True).to(device)
#model = models.mobilenet_v2(pretrained=True).to(device)
model = models.mobilenet_v3_small(pretrained=True).to(device)
#model = models.squeezenet1_1(pretrained=True).to(device)
model.eval()

# Count No. Params:
num_params = sum([np.prod(p.size()) for p in model.parameters()])
print(num_params)


# Count Latency with different batch size:
input_size = 224
#batch_size = [1, 2, 4, 8]
batch_size = [1]
latency_batch = []

for batch_s in batch_size:
	input_data = torch.rand(batch_s, 3, input_size, input_size).to(device)
	latencies =[]
	print("batch size = ", batch_s)
	
	with torch.no_grad():
		for i in range(1000):
			start = timer()
			output = model(input_data)
			end = timer()

			if (i > 0):
				latencies.append(end - start)
				print("iter {}, time = ".format(i-1), latencies[-1])
	latency_batch.append(np.mean(latencies))
	print("mean latency = {:.2f}".format(np.mean(latencies)))
	print("std latency = {:.2f}".format(np.std(latencies)))

plt.plot(batch_size, latency_batch, 'o')
plt.xlabel('Batch size')
plt.ylabel('Latency (in second)')
plt.ylim(0, np.max(latency_batch)+1)
plt.savefig("squeezenet_batch_latency.png")


# Count FLOPS
input_data = torch.rand(1, 3, input_size, input_size).to(device)
with torch.no_grad():
	count_ops(model, input_data)
	
