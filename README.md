# Object detection custom models scripts


## Table of Contents

- [Introduction](#introduction)
This repository contains scripts to train and deploy custom object detection models.

- [Annotation](#Annotation)
    -For annotation, we use `LabelImg` or `cvat.ai` for annotating images. 
    - The annotation files are saved in different formats. Personally i would suggest to use cvat.ai for annotating images. It is easy to use and has a lot of features. Tip use `n` to mark new bounding box. 
    - Make sure classes names are string.
    - Datset conversion & data auggmentation scripts are added in the utils folders.

- [Setup](#setup)
These notebooks are compatible with Google Colab. To use them, you will need to upload them to your Google Drive and open them in Google Colab.

For annotation tool, you can use labelImg for yolo format or VoTT for coco format. I have also added script in layout parser to convert to COCO format.

    - Layout Parser --> COCO Dataset Format
    - YOLO --> Yolo Dataset Format & AUGGMENTATION added in training code.
    - Detectron2 --> COCO Dataset Format

- [Comman issues Training](#training)
    - If you are using colab, make sure you have GPU enabled.
    
    Layout Parser
    - Darknet "make" error
        - Solution: Use the darket repo given in the notebook. other repos may not workon google colab.
    - For layout parser where we are using COCO dataset type. Only name of the files are needed in the train.txt and val.txt files. The path is not needed.
    - For layout parser where we are using COCO dataset type. The train.txt and val.txt files should be in the same folder as the images or can be specified by the args used in the notebook.

    Detectron2
    - Make sure classes names are string to avoid any isssues during training.

    YOLO
    - See if the the txt files in yolo format does not have any whitespaces and the file names are correct. (for example if the image name is 01.jpg then the txt file should be 01.txt, 0 is important here)

- [Deployment](#deployment)
For deployment, you will need to create a flask app and deploy it on a server. You can use the flask app in this repository as a starting point. Check the server folder for the flask app.

