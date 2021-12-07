Lab 9: Carbon footprint
===
The goal of this lab is for you estimate the carbon footprint of your class project.

Group name:
---
Group members present in lab today: Yuqing Qin (yuqingq), Yukun Xia (yukunx)

1: Inference
----
1. Plug your device in to the Kill-a-watt and run inference using your model to get a measurement of the energy draw. What is its baseline energy draw, and how does that compare to running inference?
2. Multiply energy draw by inference time to get an estimate of energy required per inference (you can average over input size).
3. Multiply this by the carbon intensity of the location of your device. You can use [this resource](https://www.epa.gov/egrid/power-profiler#/).
4. Please include at least this estimate in your final project report.

2: Training
----
1. Did your project require training a model? If so, compute that estimate as well. If you used cloud resources, you can use [this tool](https://mlco2.github.io/impact/#compute) to help estimate. Otherwise, try to use the methods discussed last class for estmating carbon footprint due to training. Show your work and explain.

Our project requires training 5 more models with different backbones. To save the time, we only run the training script 1000 iterations for each model to measure the carbon emissions. The real training will take 170,000 iterations to stop. The process to calculate carbon emissions for training is shown below:

- Measure the time for running 1000 iterations (t1), and the average energy draw from the kill-a-walt (P)
- Estimate the total time required for running 170,000 iterations (170*t1)
- Use the equation from the lecture: pt = 1.58\*time\*P (kwh) and CO2 = 0.954*pt (lbs)

Below table summarizes the work:

   Model(backbone)   | time for 1000 iter | estimated total time (170,000 iter) | avg energy draw | pt(kwh)  | CO2(lbs)
   ---               | ---                | ---                                 | ---             | ---      | ---
   baseline          |196s                | 9.25h                               | 147w            |2.149     |2.049
   mobilenet_v1      |188s                | 8.87h                               | 146w            |2.047     |1.950
   mobilenet_v2      |227s                | 10.72h                              | 140w            |2.37      |2.26
   ResNet18          |143s                | 6.75h                               | 148w            |1.579     |1.506
   SqueezeNet        |187s                | 8.83h                               | 145w            |2.023     |1.930

3: Extra
----
1. Everything else: Do you have logs you can use to estimate the amount of energy + carbon that went in to all project development? Other ways of estimating? Was your device plugged in and running for the entire semester?
2. Supply chain / lifecycle analysis: Can you estimate the additional footprint due to manufacturing hardware? Lifetime energy use of your project if it was deployed in the real world?
3. If you have a Pi or Jetson 4GB: Compare Kill-a-watt measurements to command line energy measurements, and discuuss.

[TODO] 

The summary of the power usage (J) per inference (only showing top 10 engines over our 72 experimented engines):
(the engine name below is shown as `<sp_backbone_batchSize_inputHeight_inputWidth_precision_inputSequence>`)
```
'sp_resnet18_2_120_392_FP16_seq_4': 0.386
 'sp_resnet18_1_120_392_FP16_seq_4': 0.461
 'sp_squeeze_2_120_392_FP16_seq_4': 0.479
 'superpoint_pretrained_2_120_392_FP16_seq_4': 0.489
 'superpoint_pretrained_1_120_392_FP16_seq_4': 0.494
 'sp_squeeze_1_120_392_FP16_seq_4': 0.501
 'sp_sparse_2_120_392_FP16_seq_4': 0.511
 'sp_resnet18_2_120_392_FP32_seq_4': 0.524
 'sp_mbv1_2_120_392_FP16_seq_4': 0.539
 'sp_resnet18_1_120_392_FP32_seq_4': 0.552
```
The summary of the carbon emissions (lbs) using the power usage above (only showing top 10 engines over our 72 experimented engines):
```
'sp_resnet18_2_120_392_FP16_seq_4': 1.146e-07
 'sp_resnet18_1_120_392_FP16_seq_4': 1.369e-07
 'sp_squeeze_2_120_392_FP16_seq_4': 1.421e-07
 'superpoint_pretrained_2_120_392_FP16_seq_4': 1.451e-07
 'superpoint_pretrained_1_120_392_FP16_seq_4': 1.466e-07
 'sp_squeeze_1_120_392_FP16_seq_4': 1.488e-07
 'sp_sparse_2_120_392_FP16_seq_4': 1.518e-07
 'sp_resnet18_2_120_392_FP32_seq_4': 1.554e-07
 'sp_mbv1_2_120_392_FP16_seq_4': 1.598e-07
 'sp_resnet18_1_120_392_FP32_seq_4': 1.637e-07
```
