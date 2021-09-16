Lab 1: Project Brainstorming
===
The goal of this lab is for you to work as a group to brainstorm project ideas. At the end of this exercise you should have an outline for your project proposal that you can share with others to get feedback. We will share these outlines for peer feedback in the next lab.

Group name:
---
Group members present in lab today: Yuqing Qin(yuqingq), Yukun Xia(yukunx)

1: Ideas
----
Write down 3-5 project ideas your group considered (a few sentences each). Depending on your group and process, the ideas may be very different, or they may be variations on one central idea.
 1. Optimization of SuperPoint Network
 2. Optimization of SuperGlue Network
 3. Retraining SuperPoint Network



2: Narrowing
----
Choose two of the above ideas. For each one:
1. How would this project leverage the expertise of each member of your group?

    Project idea 1: Optimization of SuperPoint Network
        
        This project will involve the visual learning, SLAM, optimization techniques. SuperPoint has the VGG-like backbone, which is something Yuqing is familiar with in visual learning, and Yukun has great experience in SLAM. We all had experience working with Jetson and some optimization knowledge. 
    
    Project idea 2: Retraining SuperPoint Network
       
       This project will involve great work in training and network design. Yuqing and Yukun are both confidence in their visual learning experience. By deploying different network architecture as backbone or modifying the current architecture, hopefully we could make the model running on Jetson Nano with acceptable performance. 
        

2. In completing this project, what new things would you learn about: (a) hardware (b) efficiency in machine learning (c) I/O modalities (d) other?
    
    Project idea 1: Optimization of SuperPoint Network
        
        We would definitely learn about a) hardware, since we have to deploy the model on Jetson Nano. We would need to look into the harware performance (power, memory usage). Also, b) efficiency in machine learning is something we will learn in the project as well. We want to try with different optimization techniques to solid our understanding of efficiency in machine learning. Other than these, we would also get some experience on different optimization techniques, and the state-of-art model deployment. 
    
    Project idea 2: Retraining SuperPoint Network
        
        If we are doing this project, we would also learn about the a). hardware. Loading model and looking at the hardware performance will be the major components in our project. Also, this project will involve b).efficiency in machine learning. The focus of this project will be mainly on the network design. Instead of utilizing optimization techniques (i.e. pruning, quantization), we would mainly focus on the optimized network module design. This project will make us learn about the state-of-art network design, and we could then deploy those ideas into this project.

3. What potential road blocks or challenges do you foresee in this project? How might you adjust the project scope in case these aspects present unsurmountable challenges?
    
    Project idea 1: Optimization of SuperPoint Network
        
        The timeline for us might be tight, since we have a lot of ideas that may want to test on. To mitigate the timeline effects, we will have a roughly timeline for each optimization techniques that we want to try. Also, we need to collect the hardware data and analyze on those data, so we will take that into account as well. Based on the timeline, we will first focus on 2 tenchniques. If we could not get both of them done by the end of the project, we will limit our project scope by only focusing on the optimization technique that has larger progress. If we have more time, then we would also try other techniques to have a comparison. 

        Also, the current SuperPoint has not been tested on mobile devices yet. We might not be able to launch it directly on Jetson. It would be hard for us to measure the baseline performance on Jetson(i.e. memory usage, run speed). We might need to start the baseline testing as soon as possible before we going forward so that we might know whether the current device is sufficient or not.
    
    Proejct idea 2: Retraining SuperPoint Network
        
        For this project, we have to have a deeper understanding the original network structure. Also, we would need to have a breadth understanding of other network structures that can be used in this project. This may require us to read through a lot of research papers, and have a thorough understanding of all these techniques. Also, training the network may take a lot of time and effort. We also need to consider about the time we have and plan everything beforehead to organize the project scale. 


4. How could you potentially extend the scope of this project if you had e.g. one more month?
    
    Project idea 1: Optimization of SuperPoint Network
        
        We would try other techniques and even change the network structure to see if there is anything we can improve on. If the techniques we try are useful, we might also try with SuperGlue network and see if they works or not. We would also test on real environment through the camera we got, which is already loaded on Jetson. 

    Project idea 2: Retraining SuperPoint Network
        
        If we have more time, we would try the optimization techniques as post-processing. Also, testing on the real data will be helpful for us to get better understanding of the improvement in real world environment. Even testing with multiple cameras can be our extended scope for this project as well. 

3: Outline
----
Choose one of the ideas you've considered, and outline a project proposal for that idea. This outline will be shared with other groups next class (Tuesday) to get feedback.

We select the first idea "Optimization of SuperPoint Network".

Your outline should include:
- Motivation

    Learning-based methods for feature detector and descriptor have been verified to have better performance than the classical methods, eg. SIFT and ORB. However, learning-based methods are typically more computationally expensive. Although on high-end GPUs, realtime operation is possible, it hasn't been thoroughly explored if cheaper edge devices, such as Jetson Nano, are capable to efficiently run these deep learning models. 

- Hypotheses (key ideas)

    By deploying the optimization techniques (i.e. quantization and distillation), SuperPoint network could work on low compute mobile device(i.e. Jetson Nano) without harming the performance too much. 

- How you will test those hypotheses: datasets, baselines, ablations, and other experiments or analyses.

    * Speed test: Calculate FPS for each optimized model
    * Performance test: Use datasets, such as KITTI and TartanAir, to benchmark the final pose estimation accuracy

    * Baseline: SuperPoint Network without optimization running on Jetson.

- I/O: What are the inputs and output modalities? What existing tools will you use to convert device inputs (that are not a core part of your project) to a format readable by the model, and vice versa?

    * Inputs: Images (either monocular or stereo)
    * Outputs: Camera poses
    * Existing tool for I/O: OpenCV's image reading function for real images, or ROS bag replay for dataset

- Hardware, including any peripherals required, and reasoning for why that hardware was chosen for this project. (This is where you will request additional hardware and/or peripherals for your project!)

    * Hardware:
        Monocular camera or stereo camera

    * Reason:
        With monocular camera only, the translation part of the estimated pose can only be a direction without scale

- Potential challenges, and how you might adjust the project to adapt to those challenges.

    - Challenge 1: No available stereo camera
    - Potential Solutions:  
        - Only test stero cases on datasets
        - Only verify and demonstrate the rotation estimation in real world
    - Challenge 2: Out-of-memory when running SuperPoint
    - Potential Solutions:
        - Move descriptor calculation from GPU to CPU after a sparse set of feature points is detected
        - Remove the descriptor part and use KLT tracker
    - Challenge 3: The given pretrained SuperPoint is not generalizable
    - Potential Solution:
        - Try idea 3 "Retraining SuperPoint Network" on more datasets

- Potential extensions to the project.

    - Try idea 3 "Retraining SuperPoint Network" and quantization-awared training.
    - Try idea 2 "Optimization of SuperGlue Network" and replace the matching method with SuperGlue