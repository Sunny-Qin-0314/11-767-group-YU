Lab 6: Group work on projects
===
The goal of this lab is for you to make progess on your project, together as a group. You'll set goals and work towards them, and report what you got done, chaellenges you faced, and subsequent plans.

Group name:
---
Group members present in lab today: Yuqing Qin (yuqingq), Yukun Xia (yukunx)

1: Plan
----
1. What is your plan for today, and this week? 

Today, we will go through the retraining process, and retrain a new superpoint model with different loss function mentioned by the training repo. Also, we would continue working on the evaluation metric with the new model.

2. How will each group member contribute towards this plan?

Yuqing is working on retraining the superpoint with a different loss function, and training with different backbone.

Yukun is working on benchmarking the new model trained, and the pretrained models available online.

2: Execution
----
1. What have you achieved today / this week? Was this more than you had planned to get done? If so, what do you think worked well?

For retraining: we are using pytorch to train SuperPoint. There are four main steps as shown below:
- Prepare COCO, HPatches, and synthetic dataset.
- Train the MagicPoint (keypoint detector) with synthetic dataset
- Use this model to export COCO pseudo labels. 
- Train SuperPoint with COCO and its pseudo label.


<p align="center">
  <img width="447" height="314" src="Screenshot from 2021-11-10 17-22-25.png" >
</p>
<p align="center">
  <em>Superpoint Validation Precision and Recall</em>
</p>

For benchmarking: (Yukun)
Models: 1. MagicLeap pretrained model  2. Another pretrained superpoint (from the repo) 3. the new model we trained


2. Was there anything you had hoped to achieve, but did not? What happened? How did you work to resolve these challenges?

We were thinking about using AWS to retrain the superpoint, but we all got rejected to increase the instances on AWS. We cannot use P instances right now. Therefore, Yuqing is using her laptop with NVIDIA 2070 Super to train the model. The synthetic model training takes us about 7 hours to train, and the full Superpoint takes us 24 hours to train. 

3. What were the contributions of each group member towards all of the above?

Yukun is working on benchmarking the performance with different models we got.
Yuqing is working on retraining the superpoint with different variations.

3: Next steps
----
1. Are you making sufficient progress towards completing your final project? Explain why or why not. If not, please report how you plan to change the scope and/or focus of your project accordingly.

Yes. We are working on benchmarking the different variants of SuperPoint models. We are trying to collect as much as possible models to benchmark on.

2. Based on your work today / this week, and your answer to (1), what are your group's planned next steps?

Keep working on retraining the models, and collecting a few SuperPoint models and benchmarking them on Jetson.

3. How will each group member contribute towards those steps? 

Yuqing will continue working on retraining the network.
Yukun will continue working on benchmarking the model performance from retraining.
We will work together on the deployment.
