# tf_object_detection [![PyPI version][pypi-image]][pypi] [![Build Status][travis-image]][travis]

[travis-image]: https://travis-ci.org/junjuew/tf_object_detection.svg?branch=master
[travis]: http://travis-ci.org/junjuew/tf_object_detection

[pypi-image]: https://badge.fury.io/py/tf-object-detection.svg
[pypi]: https://pypi.org/project/tf-object-detection/

This is a thin wrapper around [Tensorflow Object Detection API](https://github.com/tensorflow/models/tree/master/research/object_detection) for easy installation and use. The original [installation procedure](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md) contains multiple manual steps that make dependency management difficult. This repository creates a pip package that automate the installation so that you can install the API with a single pip install.

## Installation

```
pip install tf-object-detection[tf]

```

Or for tensorflow with GPU support,

```
pip install tf-object-detection[tf-gpu]

```

## Usage

All the scripts from tensorflow object detection APIs work out-of-box. 
You can find an example usages from the API's [model_main.py](https://github.com/tensorflow/models/blob/master/research/object_detection/model_main.py).

```
import object_detection
```


## What's in here

* [setup.py](setup.py): The python packaging script.
* `PROTOC` Environment variable should be set so that `setup.py` can compile as
  part of the `setup.py` execution.

```bash
# Download and setup all required dependencies required for tensorflow object 
# detection libarary to work correctly.
$ python setup.py install
```

* tf_object_detection: A git submodule pointing to the version of tensorflow object detection this thin wrapper is for.
