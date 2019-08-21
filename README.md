# tf_object_detection

A Thin Wrapper around Tensorflow Object Detection API for Easy Installation and Use

## Installation

```
pip install tf-object-detection
```

## Usage

All the scripts from tensorflow object detection APIs work out-of-box. 
You can find example scripts using the API [here](tf_object_detection/research/object_detection/model_main.py).

```
import object_detection
```


## Generating 

[pb2](pb2) contains the compiled protobuf files from the following commands.

```bash
cd tf_object_detection/research/
protoc object_detection/protos/*.proto --python_out=.
mv object_detection/protos/*_pb2.py ../../pb2/
```
