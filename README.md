# object-detection-custom-models-scripts


## Table of Contents

- [Introduction](#introduction)
This repository contains scripts to train and deploy custom object detection models.

- [Setup](#setup)
These notebooks are compatible with Google Colab. To use them, you will need to upload them to your Google Drive and open them in Google Colab.

for annotation tool, you can use labelImg for yolo format or VoTT for coco format. I have alos added script in layout parser to convert to COCO format.

    - Layout Parser --> COCO Dataset Format
    - YOLO --> Yolo Dataset Format

- [Comman issues Training](#training)
    - Darknet "make" error
        - Solution: Use the darket repo given in the notebook. other repos may not workon google colab.
    - For layout parser where we are using COCO dataset type. Only name of the files are needed in the train.txt and val.txt files. The path is not needed.
    - For layout parser where we are using COCO dataset type. The train.txt and val.txt files should be in the same folder as the images or can be specified by the args used in the notebook.


- [Deployment](#deployment)
For deployment, you will need to create a flask app and deploy it on a server. You can use the flask app in this repository as a starting point. Check the server folder for the flask app.

