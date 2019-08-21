# tf_object_detection

This is a thin wrapper around [Tensorflow Object Detection API](https://github.com/tensorflow/models/tree/master/research/object_detection) for easy installation and use. The original [installation procedure](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md) contains multiple manual steps that make dependency management difficult. This repository creates a pip package that automate the installation so that you can install the API with a single pip install.

## Installation

```
pip install tf-object-detection
```

## Usage

All the scripts from tensorflow object detection APIs work out-of-box. 
You can find an example usages from the API's [model_main.py](https://github.com/tensorflow/models/blob/master/research/object_detection/model_main.py).

```
import object_detection
```


## What's in here

* [setup.py](setup.py): The python packaging script.
* [pb2](pb2): This directory contains the compiled protobuf files from the following commands.

```bash
cd tf_object_detection/research/
protoc object_detection/protos/*.proto --python_out=.
mv object_detection/protos/*_pb2.py ../../pb2/
```
* tf_object_detection: A git submodule pointing to the version of tensorflow object detection this thin wrapper is for.
