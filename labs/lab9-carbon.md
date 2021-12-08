Lab 9: Carbon footprint
===
The goal of this lab is for you estimate the carbon footprint of your class project.

Group name:
---
Group members present in lab today: Yuqing Qin (yuqingq), Yukun Xia (yukunx)

1: Inference
----
1. Plug your device in to the Kill-a-watt and run inference using your model to get a measurement of the energy draw. What is its baseline energy draw, and how does that compare to running inference?

Answer:

| Configuration          | Energy Draw (Watt) |
|------------------------|--------------------|
| Baseline               | 3.40               |
| SuperPoint MobileNetv1 | 7.00               |
| SuperPoint MobileNetv2 | 7.90               |
| SuperPoint SqueezeNet  | 6.35               |
| SuperPoint ResNet18    | 5.50               |

By comparison, running the inference will increase the energy draw from the baseline by 2.1~4.5W.


2. Multiply energy draw by inference time to get an estimate of energy required per inference (you can average over input size).

| Configuration          | Energy Draw (Watt) | Latency (s) | Energy per Inference (J) |
|------------------------|--------------------|-------------|--------------------------|
| SuperPoint MobileNetv1 | 7.00               | 0.085       | 0.595                    |
| SuperPoint MobileNetv2 | 7.90               | 0.101       | 0.798                    |
| SuperPoint SqueezeNet  | 6.35               | 0.065       | 0.413                    |
| SuperPoint ResNet18    | 5.50               | 0.058       | 0.319                    |

Note that here all models are running on 120x392 images.

3. Multiply this by the carbon intensity of the location of your device. You can use [this resource](https://www.epa.gov/egrid/power-profiler#/).

| Configuration          | Energy per Inference (J) | CO2(lbs)      |
|------------------------|--------------------------|---------------|
| SuperPoint MobileNetv1 | 0.595                    | 1.7646e-7 |
| SuperPoint MobileNetv2 | 0.798                    | 2.3667e-7 |
| SuperPoint SqueezeNet  | 0.413                    | 1.2248e-7 |
| SuperPoint ResNet18    | 0.319                    | 9.4610e-8 |

Using the local carbon intensity: CO2 = 1067.7(lbs/MWh) * energy

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

We only have log files for the final results, but we can estimate the time usage of each device, and multiply it by a reasonable power value. We also didn't plug in our Jetson most of the time, and do our development and training on our laptops.

2. Supply chain / lifecycle analysis: Can you estimate the additional footprint due to manufacturing hardware? Lifetime energy use of your project if it was deployed in the real world?

The manufacture of Jetson Nanos can be roughtly divided into the chip and electronics part and the auxiliary material part. We can measure the volume or count the item numbers on our Jetson Nano, but it requires some extra investigation on the carbon footprint formula. For example, it's very hard to count the carbon footprint from R&D, and also the formula could be dependent on the factory location.


3. If you have a Pi or Jetson 4GB: Compare Kill-a-watt measurements to command line energy measurements, and discuuss.

| Configuration          | Energy per Inference from Kill-A-Watt (J) | Energy per Inference from Command Line (J) |
|------------------------|-------------------------------------------|--------------------------------------------|
| SuperPoint MobileNetv1 | 0.595                                     | 0.528                                      |
| SuperPoint MobileNetv2 | 0.798                                     | 0.683                                      |
| SuperPoint SqueezeNet  | 0.413                                     | 0.358                                      |
| SuperPoint ResNet18    | 0.319                                     | 0.281                                      |

All the results from Kill-A-Watt are slightly larger than the one reading from command line. The two methods may have different measurement principles and generally, the two sets of results are close to each other.
