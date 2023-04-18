# Mario Kart A.I. Driver 


This is a repo containing several agents to attempt to drive autonomously in mario kart. 

See our paper outlining the code at: 
https://docs.google.com/document/d/1Ne4uVVX_DXk6bUaqH9qNLk1GzTmPJaFlKLCuyeSxT7o/edit 

The structure is as follows:

* driver.py: The main code for crawling the website we are running the agent on and serves as our controller 
* ImageProcessor.py: Helper file for processing images supporting functionality such as cropping and reformatting large numbers of images 
* ImageSegmentation.ipynb: The notebook where we tested image segmentation and built our UNET Model  
* ImitationDriver.py: Our Code version of our imitation notebook that loads in a trained model and generates predictions on what moves to make 
* ImitationLearning.ipynb: The notebook we used to explore imitation learning and where we trained our imitation model 
* ObjectDetection.ipynb: Exploratory notebook where we examined pre-built models initially 
* SegmentationAI.py: The main python code for generating segmentation maps. 