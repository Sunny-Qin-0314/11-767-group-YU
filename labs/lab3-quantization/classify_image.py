import torchvision.models as models
import torch
from torchvision import transforms
from PIL import Image

labels = [line.strip() for line in open("imagenet_labels.txt")]
model = models.quantization.mobilenet_v2(pretrained=True, quantize=True)
#model = models.quantization.resnet18(pretrained=True, quantize=False)
#model = models.mobilenet_v3_small(pretrained=True)
#model = models.squeezenet1_1(pretrained=True).to(device)
model.eval()

#quantized_model = torch.quantization.quantize_dynamic(model, {torch.nn.Linear}, dtype=torch.qint8)


#transform = transforms.Compose([transforms.Resize(255),
#                               transforms.CenterCrop(224),
#                                transforms.ToTensor()])

#normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406],
#                                std=[0.229, 0.224, 0.225])

#image = Image.open("image.jpg").convert('RGB')
#image = transform(image)
#image = normalize(image)
#image = image.unsqueeze(0)


#out = model(image)
#label = labels[torch.argmax(out[0]).item()]
#print(f"Found a {label}")


# Count Latency with different batch size:
input_size = 224
batch_size = [1, 2, 4, 8]
#batch_size = [1]
latency_batch = []

for batch_s in batch_size:
    input_data = torch.rand(batch_s, 3, input_size, input_size)
    latencies =[]
    print("batch size = ", batch_s)
    
    with torch.no_grad():
        for i in range(11):
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