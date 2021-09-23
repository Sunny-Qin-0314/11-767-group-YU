Lab 2: Project Workshopping / Peer Feedback
===
The goal of this lab is for you to give and receive peer feedback on project outlines before writing up your proposal. 

- **You can find your team's reviewing assignments in the first sheet [here](https://docs.google.com/spreadsheets/d/1_pw_lYkFutMjuL1_j6RdxNyQlj7LvF_f5eEKr1Qm-w0/edit?usp=sharing).**
- **The second sheet contains links to all teams' outlines to review.**
- **Once you have reviewed an outline, please enter a link to your review (e.g. a Google Doc, public github repo, etc.) replacing your team name in the corresponding other team's row in the third sheet.**


Here's a reminder of what your completed project proposal should include:
- Motivation
- Hypotheses (key ideas)
- How you will test those hypotheses: datasets, ablations, and other experiments or analyses.
- Related work and baselines
- I/O: What are the inputs and output modalities? What existing tools will you use to convert device inputs (that are not a core part of your project) to a format readable by the model, and vice versa?
- Hardware, including any peripherals required, and reasoning for why that hardware is needed for this project. (This is where you will request additional hardware and/or peripherals for your project!)
- Will you need to perform training off-device? If so, do you need cloud compute credits (GCP or AWS), and how much?
- Potential challenges, and how you might adjust the project to adapt to those challenges.
- Potential extensions to the project.
- Potential ethical implications of the project.
- Timeline and milestones. (Tip: align with Thursday in-class labs!)

Group name:
---
Group members present in lab today: Yuqing Qin (yuqingq), Yukin Xia (yukunx)

1: Review 1
----
Name of team being reviewed: TQL
1. How does your team's background align with that of the proposed project (e.g. if the proposed project is in CV but your team's backgorund is mostly NLP, state that here. Similarly, if your team also has someone who specializes in the area of the proposed project, state that here.)

Our team has background in CV.


2. Are the motivation, hypotheses, and plan to test those hypotheses clear? If not, where could the team provide more clarification or explanation? 

The motivation and hypotheses are clear. One suggestion is that it would be better to give the related reference/more details to the compression approach you proposed so that we could know more about how this approach could help with your model running.

Also, the 'degree of compression' in the testing section is a little bit unclear. It would be better to clarify this term in details.

3. Does the project seem properly scoped for a semester-long project? Why or why not? How might the team be able to adjust the project to be appropriately scoped?

We are worried about the scope a little bit, since you might need to retrain the smaller model, instead of using the entire pretrained model from the paper. It would be better to have a clear timeline about those training and experiments. 

4. Are there any potential ethical concerns that arise from the proposed project? 

Not see those concerns in this project.

5. Any additional comments or concerns? Any related work you know of that might be relevant and/or helpful?
N/A

2: Review 2
----
Name of team being reviewed: NoName
1. How does your team's background align with that of the proposed project (e.g. if the proposed project is in CV but your team's backgorund is mostly NLP, state that here. Similarly, if your team also has someone who specializes in the area of the proposed project, state that here.)

The proposal covers both CV and NLP tasks, and our team has knowledge on the CV part.

2. Are the motivation, hypotheses, and plan to test those hypotheses clear? If not, where could the team provide more clarification or explanation? 

The motivation and hypotheses are pretty clear, but the test plan needs to narrow down a little. For example, the proposal mentioned both CV and NLP datasets, and it'd be more practical to firstly focus on one of IO modalities, and set others as stretch goals. As their key improvement stays at the deserialization, NLP models are typically larger and thus NLP tasks could be more suitable for the initial testing.
Model selection for each benchmarking will also need some effort as well. It would be better to have a range of models you want to work on. 

3. Does the project seem properly scoped for a semester-long project? Why or why not? How might the team be able to adjust the project to be appropriately scoped?

This project could be a little ambitious since the deserialization methods won’t be covered in class, but if there’s anyone in the team with a strong background on this topic, the scope should be fine. Again, it will cover NLP, CV, and multimodal, it would be hard to have all these covered during the semester. If you want to have those experimenting in parallel, you might need more devices at the same time to test on. It is also time-consuming.

4. Are there any potential ethical concerns that arise from the proposed project? 

No

5. Any additional comments or concerns? Any related work you know of that might be relevant and/or helpful?

No

3: Review 3
----
Name of team being reviewed: Hagrids
1. How does your team's background align with that of the proposed project (e.g. if the proposed project is in CV but your team's backgorund is mostly NLP, state that here. Similarly, if your team also has someone who specializes in the area of the proposed project, state that here.)

Our team’s backgrounds are mostly in CV. 

2. Are the motivation, hypotheses, and plan to test those hypotheses clear? If not, where could the team provide more clarification or explanation? 

The motivation is clear. The hypothesis looks good to us.
It’s not that much clear to us that the performance measurement is done during the deployment on Jetson or before the deployment. Like the ‘inference time’ in your testing plan, will that be better to test when you deploy the model on Jetson? 

3. Does the project seem properly scoped for a semester-long project? Why or why not? How might the team be able to adjust the project to be appropriately scoped?

Yes. The goals of the project are separate into the main part and potential extensions. The main part is to downscale the Allosaurus model with distillation, pruning, and adaptive training. The distillation and pruning will be covered in class, so this part should be practical for a semester-long project.

4. Are there any potential ethical concerns that arise from the proposed project? 

No

5. Any additional comments or concerns? Any related work you know of that might be relevant and/or helpful?

No

4: Receiving feedback
----
Read the feedback that the other groups gave on your proposal, and discuss as a group how you will integrate that into your proposal. List 3-5 useful pieces of feedback from your reviews that you will integrate into your proposal:
1. Concerns about out of memory issue: we currently consider about the alternatives on how to load the model if there is any out of memory happened (i.e. seperate the feature extraction and descriptor generation; or only generate the interested point's descriptor instead of all image pixel descriptor)
2. Include current model benchmark performance as baseline: we are looking into those concrete benchmark right now. Since SuperPoint has not been tested on any model devices (Jetson), we might also need to test it by ourself.
3. Include details about how to deploy optimization techniques: we will narrow down the scope and the specific optimization techniques we will be using, and the details on how to combine it with SuperPoint.
4. Include more details about post-evaluation

You may also use this time to get additional feedback from instructors and/or start working on your proposal.


