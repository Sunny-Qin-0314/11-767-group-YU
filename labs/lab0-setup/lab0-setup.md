Lab 0: Hardware setup
===
The goal of this lab is for you to become more familiar with the hardware platform you will be working with this semester, and for you to complete basic setup so that everyone in the group should be able to work remotely on the device going forward. By the end of class today, everyone in your group should be able to ssh in to the device, use the camera to take a picture, record audio, run a basic NLP model, and run a basic CV model. 

If you successfully complete all those tasks, then your final task is to write a script that pipes together I/O with a model. For example, you could write a script that uses the camera to capture an image, then runs classification on that image. Or you could capture audio, run speech-to-text, then run sentiment analysis on that text.

Group name: Group-YU
---
Group members present in lab today: Yuqing Qin, Yukun Xia

1: Set up your device.
----
Depending on your hardware, follow the instructions provided in this directory: [Raspberry Pi 4](https://github.com/strubell/11-767/blob/main/labs/lab0-setup/setup-rpi4.md), [Jetson Nano](https://github.com/strubell/11-767/blob/main/labs/lab0-setup/setup-jetson.md), [Google Coral](https://coral.ai/docs/dev-board/get-started/). 
1. What device(s) are you setting up?

    A: Jetson Nano 2GB

2. Did you run into any roadblocks following the instructions? What happened, and what did you do to fix the problem?

    A: Yes. 

    Problem 1: After system image was written into SD card, we powered on Jetson Nano, but it failed to boot and was stuck at `A start job is running for End-user configuration after initial OEM installation (10min 25s / no limit)`. The solution was to press `pressed ctrl+alt+del`.

    Problem 2: Initially, `sudo apt -y install curl` was not runnable, and we had to enable `Source code` in `Software & Updates`.

    Problem 3: `torchvision` was not automatically installed with pytorch, and its installation script was not written in the setup-jetson.md. We tried a [thrid-party tutorial](https://qengineering.eu/install-pytorch-on-jetson-nano.html) with precompiled wheel provided, but we failed at installing the wheel, with an error message `error: package directory 'torch/cuda' does not exist`. Then we tried the [Nvidia's instruction](https://forums.developer.nvidia.com/t/pytorch-for-jetson-version-1-9-0-now-available/72048) to build `torchvision` from scratch. The commands we ran were documented in the following.
    ```
    $ sudo apt-get install libjpeg-dev zlib1g-dev libpython3-dev libavcodec-dev libavformat-dev libswscale-dev
    $ git clone --branch release/0.10.0 https://github.com/pytorch/vision torchvision   # see below for version of torchvision to download
    $ cd torchvision
    $ export BUILD_VERSION=0.10.0  # where 0.x.0 is the torchvision version  
    $ python3 setup.py install --user
    $ cd ../  # attempting to load torchvision from build dir will result in import error
    ```

3. Are all group members now able to ssh in to the device from their laptops? If not, why not? How will this be resolved?

    A: Yes

2: Collaboration / hardware management plan
----
4. What is your group's hardware management plan? For example: Where will the device(s) be stored throughout the semester? What will happen if a device needs physical restart or debugging? What will happen in the case of COVID lockdown?

    Location: We'll keep our Jetson Nano at the MRSD Lab in the basement of NSH.

    Physical Operation: Yuqing and Yukun are both MRSD students, and we'll usually will stay in the MRSD Lab. 

    COVID Lockdown: MRSD Lab is large enough to maintain social distancing, so our group progress is not likely to be affected by potential lockdown.


3: Putting it all together
----
5. Now, you should be able to take a picture, record audio, run a basic computer vision model, and run a basic NLP model. Now, write a script that pipes I/O to models. For example, write a script that takes a picture then runs a detection model on that image, and/or write a script that . Include the script at the end of your lab report.

    

6. Describe what the script you wrote does (document it.) 
7. Did you have any trouble getting this running? If so, describe what difficulties you ran into, and how you tried to resolve them.

