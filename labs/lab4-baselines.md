Lab 4: Baselines and Related Work
===
The goal of this lab is for you to survey work related to your project, decide on the most relevant baselines, and start to implement them.

Ideally, the outcome of this lab would be: (1) the related work section of your project report is written and (2) baselines have been benchmarked.

Group name:
---
Group members present in lab today: Yuqing Qin, Yukun Xia

1: Related Work
----
1. Choose at least 2 pieces of related work per group member. For each piece of related work, write a paragraph that includes:
    - Summary of the main contributions of that work.
    - How your proposed project builds upon or otherwise relates to that work.
    
    * Paper 1: [SuperPoint: Self-Supervised Interest Point Detection and Description](https://arxiv.org/pdf/1712.07629.pdf)
        * Contribution summary
            * Superpoint is a deep learning feature point detector with self-supervised learning. Real images with different homography warpings will be used to detect feature points, and then the repeatable features will be collected as the training target. This process can be repeated to keep refining the detector.
        * Relationship to the proposed project
            * This paper will serve as the baseline of the proposed project
    * Paper 2: [UnsuperPoint: End-to-end Unsupervised Interest Point Detector and Descriptor](https://arxiv.org/pdf/1907.04011.pdf)
        * Contribution summary
            * Formulate the deep learning feature point detection as a regression rather than a classification problem. The authors claimed that its performance surpassed SuperPoint.
        * Relationship to the proposed project
            * An extension to this project

2: Baselines
----
1. What are the baselines that you will be running for your approach? Please be specific: data, splits, models and model variants, any other relevant information.
2. These baselines should be able to run on your device within a reasonable amount of time. If you haven't yet tried to run them, please include a back-of-the-envelope calculation of why you think they will fit in memory. If the baselines will not fit in memory, return to (1) and adjust accordingly.
3. How will you be evaluating your baselines?
4. Implement and run the baselines. Document any challenges you run into here, and how you solve them or plan to solve them.
5. If you finish running and evaluating your baselines, did the results align with your hypotheses? Are there any changes or focusing that you can do for your project based on insights from these results?

3: Extra
----
More related work, more baselines, more implementation, more analysis. Work on your project.


FAQ
----
1. Our baseline is the SotA model from XXX 2021 which doesn't fit on device.  

Yikes! I think you meant to say -- "We used some very minimal off the shelf components from torchvision/huggingface/... to ensure our basic pipeline can run"

2. We're evaluating our baseline on accuracy only

I think you meant to say -- "We plan to plot accuracy against XXXX to see how compute and performance trade-off. Specifically, we can shrink our baseline by doing YYYY"
