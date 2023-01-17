# YOLO_GA
A simulation platform that sythensize tools that applies object-detection(yolo) onto cloud-gaming system(gaminganywhere)

## Tutorial
In Linux command line terminal, set the environment variable `PYTHONPATH`   
```
export PYTHONPATH='$(your own working path)/yolo_ga'
```
Then you can run any unit tests.


## Project Directory Tree
```
├── README.md
├── config.py
├── goi_dir
│   └── goi0
│       ├── bdboxs
│       │   └── $(index).txt
│       ├── ffmpeginfo
│       │   ├── MotionVector.txt
│       │   └── frame_type.txt
│       └── imgs
│           └── $(index).png
├── main
│   ├── bdbox.py
│   ├── goi.py
│   └── motion_vector.py
├── sim
│   └── disp_imgs.py
├── test
│   ├── bdbox_test.py
│   ├── chart_test.py
│   ├── disp_test.py
│   ├── goi_test.py
│   ├── parse_test.py
│   └── test.py
└── utils
    ├── chart.py
    ├── parse.py
    └── tools.py
```
The whole project aims to process images captured by gaminganywhere. The raw input should be a sequence of consecutive game frames, stored in `goi_dir/goi$(i)` currently only one goi(group of information/images).
### goi_dir
goi stands for group of information. 
Below is the table of correspondence between goi and its game.
| goi index | goi path     | Game name |
|:---------:|--------------|:---------:|
|     0     | goi_dir/goi0 | Neverball |

Besides images themselves, we need extra information from 1.ffmpeg 2.yolo to map the bounding boxes, therefore currently each goi has three subdirectories:
* imgs

    Storing the consecutive images of a game, in png format.
* bdboxs

    Storing the information of bounding boxes detected by yolo, each txt file corresponds to a game frame in imgs/

    **TODO: Merge yolo program into the project, so that we do not need an extra folder under goi, instead we directly generate bdboxs information in runtime**

* ffmpeginfo

    Storing the ffmpeg-related information.
    * frame_type.txt
        
        Each line indicates the frame type of each frame in imgs/
        There are totally three kinds:I-frame, B-frame, P-frame. I,P frames are called reference frame, B frame is non-reference frame.
    * MotionVector.txt

        Storing the inter-frame MotionVector for every game frame.

    **TODO: Merge the modified ffmpeg program into the project, so that we do not need an extra folder under goi, instead we directly generate ffmpeg information in runtime**

### main
Main part of the project. Includes all the project-related data structures and functions here.
* bdbox.py

    A self-defined class for boundingbox, it has only one member function: `split_img_bdboxs` which takes a list of bdboxs and an image as input, output all the pixel positions in the format of (x,y) that are in the bounding boxs.
* goi.py

    A self-defined class for goi, all important functions are in here.
    It is implemented by a self-defined data structure Chart, for details of this data structure please refer to [this](utils/CHART.md)  

* motion_vector.py

    A self-defined class for motion-vector.

**TODO: Add ffmpeginfo into main/**

### sim

Simulation functions. Not neccessary, only for visualization purpose.

* disp_imgs.py

    functions to display a set of consecutive images.

### test
Unit tests, after finishing a module, write a unit test in this folder and make sure it runs as expected.

### utils
Any Useful functions and tools that can be reused in several modules should be placed here. 
* parse.py

    functions that parse txt/img files in goi_dir/
* chart.py

    A self-defined data structures, for details please refer to [this](utils/CHART.md)
* tools.py
  
    Other useful tools.
