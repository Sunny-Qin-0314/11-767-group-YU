Lab 3: Quantization
===
The goal of this lab is for you to benchmark and compare model size and inference efficiency **between quantized and original models** on your devices. You should benchmark the same models as you benchmarked last lab, so ideally **2*N* models or model variants, where *N* is the size of your group (so, two models per person.)** For now, if you don't have appropriate evaluation data in place that's fine; you can provide pretend data to the model for now and just evaluate efficiency.

Ideally, the models you benchmark will be the same as last class, but if you find that you're unable to run out-of-the-box quantization on your models, feel free to try quantizing other models, or a subset. Just be sure to explain what you tried, and why.

Include any code you write to perform this benchmarking in your Canvas submission (either as a link to a folder on github, in a shared drive, zip, etc).

Group name:
---
Group members present in lab today: Yuqing Qin (yuqingq), Yukun Xia (yukunx)

1: Models
----
1. Which models and/or model variants will your group be studying in this lab? What is the original bit width of the models, and what precision will you be quantizing to? What parts of the model will be quantized (e.g. parameters, activations, ...)? Please be specific.

The model we used:

- MobileNet v2: from fp32 to int8. Quantize the parameters
- MobileNet v3_small: from fp32 to int8, Quantize the parameters
- ResNet18: from fp32 to int8, quantize the parameters
- SqueezeNet: from fp32 to int8, quantize the parameters


2. Why did you choose these models?

These four model are chosen by the last lab. It would be easy to quantize these models and compare with the performance we measure last time. Also, since our project is about changing the backbone to a smaller network. If we could quantize the smaller network further, we could save more memeory then. Once we have the quantized version, we could directly use them in our project.

3. For each model, you will measure model size (in (mega,giga,...)bytes), and inference latency. You will also be varying a parameter such as input size or batch size. What are your hypotheses for how the quantized models will compare to non-quantized models according to these metrics? Do you think latency will track with model size? Explain.

From the last lab, we saw that ResNet18 and squeezenet runs faster than mobilenetv3 and v3_small. We are expecting the quantized mobilenet would reach the similar performance we saw from ResNet and SqueezeNet. Also, the ResNet and SqueezeNet can be further quantized to reduce their memory usage. ResNet model is the one with the most expensive memory usage compared to the other threes. We are expecting the quantized ResNet would have a smaller model size. Regarding the latency, since the quantized model will have a smaller model size and small memory usage, the latency will also be decreased. When loading the model into memory and do the calculation, the low precision model will have less operations, which will make it run faster. 


2: Quantization in PyTorch
----
1. [Here is the official documentation for Torch quantization](https://pytorch.org/docs/stable/quantization.html) and an [official blog post](https://pytorch.org/blog/introduction-to-quantization-on-pytorch/) about the functionality. Today we'll be focusing on what the PyTorch documentation refers to as  **dynamic** quantization (experimenting with **static** quantization and **quantization-aware training (QAT)** is an option for extra credit if you wish). 

2. In **dynamic** PyTorch quantization, weights are converted to `int8`, and activations are converted as well before performing computations, so that those computations can be performed using faster `int8` operations. Accumulators are not quantized, and the scaling factors are computed on-the-fly (in **static** quantization, scaling factors are computed using a representative dataset, and remain quantized in accumulators). You can acitvate dynamic quantization to `int8` for a model in PyTorch as follows: 
   ```
   import torch.quantization
   quantized_model = torch.quantization.quantize_dynamic(model, {torch.nn.Linear}, dtype=torch.qint8)
   ```
3. Make sure you can use basic quantized models. Dynamic quantization using torchvision is quite straightforward. e.g. you should be able to run the basic [`classify_image.py`](https://github.com/strubell/11-767/blob/main/labs/lab3-quantization/classify_image.py) script included in this directory, which uses a quantized model (`mobilenet_v2`). If you are having trouble, make sure your version of torch has quantization enabled. This whl should work:
    ```
    wget herron.lti.cs.cmu.edu/~strubell/11-767/torch-1.8.0-cp36-cp36m-linux_aarch64.whl
    pip3 install torch-1.8.0-cp36-cp36m-linux_aarch64.whl
    ```
4. Try changing the model to `mobilenet_v3_large` and set `quantize=False`. (Note that `quantize=True` may fail due to unsupported operations.) What happens?

When we set up the `quantize=True` on Jetson, we got `segmentation fault` due to limited memory avaiable. We retried on Google Colab, when set `quantize=False`, the model size remains the same as the unquantized version. This means when we set it parameter to be false, it will run the unquantized operation.

5. Try to use this to quantize your models. If you're feeling lost and/or you're unable to get this to work on your model [here is a tutorial on using dynamic quantization on a fine-tuned BERT](https://pytorch.org/tutorials/intermediate/dynamic_quantization_bert_tutorial.html) and [here is one quantizing an LSTM language model](https://pytorch.org/tutorials/advanced/dynamic_quantization_tutorial.html). 

6. Any difficulties you encountered here? Why or why not?

We tried to quantized our models on Jetson. It always failed by `segmentation fault` due to limited memory. Jetson is the edge device, we should apply every quantization or training processes on other devices, and only use Jetson when we decided to deploy the model.

3: Model size
----
1. Compute the size of each model. Given the path to your model on disk, you can compute its size at the command line, e.g.:
   ```
   du -h <path-to-serialized-model>
   ```

   Model             | Size (before quantization) | Size (after quantization)
   ---               | ---                        | ---
   mobilenet_v2      | 14M                        | 3.5M
   MobileNetv3_small | 10.3M                      | 5.46M
   ResNet18          | 46.8M                      | 45.29M
   SqueezeNet        | 4.96M                      | 4.96M


2. Any difficulties you encountered here? Why or why not?

We first tried to do the quantization on Jetson, which failed due to the limited memory. Our RAM usage is almost full in Jetson. Therefore, we did the quantization on our own laptop and deploy the quantized model on Jetson instead. SqueezeNet does not contain linear layer, only convolutional layer, therefore it cannot be quantized by current dynamic quantization (pytorch currently only support `linear` and `LSTM` layer for dynamic quantization)

4: Latency
----
1. Compute the inference latency of each model. You can use the same procedure here as you used in the last lab. Here's a reminder of what we did last time: 
   You should measure latency by timing the forward pass only. For example, using `timeit`:
    ```
    from timeit import default_timer as timer

    start = timer()
    # ...
    end = timer()
    print(end - start) # Time in seconds, e.g. 5.38091952400282
    ```
    Best practice is to not include the first pass in timing, since it may include data loading, caching, etc.* and to report the mean and standard deviation of *k* repetitions. For the purposes of this lab, *k*=10 is reasonable. (If standard deviation is high, you may want to run more repetitions. If it is low, you might be able to get away with fewer repetitions.)
    
    For more information on `timeit` and measuring elapsed time in Python, you may want to refer to [this Stack Overflow post](https://stackoverflow.com/questions/7370801/how-to-measure-elapsed-time-in-python).


   Model (quantized) |Latency(in seconds)
   ---               | ---                       
   mobilenet_v2      | 0.0495                        
   MobileNetv3_small | 0.0139                    
   ResNet18          | 0.1004                     
   SqueezeNet        | 0.03 (same as not quantized version)                    



2. Repeat this, varying one of: batch size, input size, other. Plot the results (sorry this isn't a notebook):
   ```
   import matplotlib.pyplot as plt
   
   plot_fname = "plot.png"
   x = ... # e.g. batch sizes
   y = ... # mean timings
   
   plt.plot(x, y, 'o')
   plt.xlabel('e.g. batch size')
   plt.ylabel('efficiency metric')
   plt.savefig(plot_fname)
   # or plot.show() if you e.g. copy results to laptop
   ```

   2.1 MobileNetv2

   ![MobileNetv2](./mobilenetv2_batch_latency.png)

   2.2 MobilevNet3_small

   ![MobilevNet3_small](./mobilev3_small_batch_latency.png)

   2.3 Resnet18

   ![Resnet18](./resnet_batch_latency.png)

   2.4 SqueezeNet

   ![SqueezeNet](./squeezenet_batch_latency.png)

4. Any difficulties you encountered here? Why or why not?

   Again, Jetson cannot load larger batch size (i.e. 8), we have to run the whole comparison on Google Colab. When tried with larger batch size, Jetson will run out of memory and get `segmentaion fault`.

5: Discussion
----
1. Analyze the results. Do they support your hypotheses? Why or why not? Did you notice any strange or unexpected behavior? What might be the underlying reasons for that behavior?

Most of the experiments aligned with our expectation. We do see the mobilenet benefits a lot from quantization. For model size, mobilenet after quantization is almost half its size compared to the one before quantization. For latency, we also see the MobileNet runs much faster compared to last time. SqueezeNet does not have `linear` layer, so it cannot be quantized by pytorch `dynamic quantization`. Also, surprisingly, the unquantized SqueezeNet has smaller size compared to MobileNetv3_small, but it runs much slower than it. This observation means that the latency does not have direct relationship with the model size. ResNet only benefits a little bit from quantization since it has limited number of `linear` layer. The model size of ResNet is slightly smaller, the latency is almost the same.

5: Extra
----
A few options:
1. Try to run static quantization, or quantization aware training (QAT). Benchmark and report your results. Here is a nice blog post on [using static quantization on Torchvision models](https://leimao.github.io/blog/PyTorch-Static-Quantization/) in PyTorch.
2. Compute FLOPs and/or energy use (if your device has the necessary power monitoring hardware) for your models. 
3. Evaluate on different hardware (for example, you might run the same benchmarking on your laptop.) Compare the results to benchmarking on your device(s).
4. Use real evaluation data and compare accuracy vs. efficiency. Describe your experimental setup in detail (e.g. did you control for input size? Batch size? Are you reporting average efficiency across all examples in the dev set?) Which model(s) appear to have the best trade-off? Do these results differ from benchmarking with synthetic data? Why or why not?

----
\* There are exceptions to this rule, where it may be important to include data loading in benchmarking, depending on the specific application and expected use cases. For the purposes of this lab, we want to isolate any data loading from the inference time due to model computation.
