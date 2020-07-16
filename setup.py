import glob
import sys
import os
import shutil
from distutils.spawn import find_executable
import setuptools
import subprocess
from typing import List

file_dir = os.path.dirname(os.path.realpath(__file__))


def runcmd(cmds: List[str]):
    return subprocess.call(cmds, shell=True)


# Find the Protocol Compiler.
if 'PROTOC' in os.environ and os.path.exists(os.environ['PROTOC']):
  protoc = os.environ['PROTOC']
else:
  protoc = find_executable("protoc")

if not protoc:
    error = "protoc command not found in PATH."\
    " install the protoc command system wide or set the PROTOC env"\
    " variable with protoc executable path."
    print(error)
    sys.exit(1)

proto_commands = [
    "cd ./tf_object_detection/research;" +
    protoc +
    " object_detection/protos/*.proto" +
    " --python_out=."
]
# Pull the upstream object_detection code and package it.
runcmd(['git', 'submodule', 'update', '--init'])
runcmd(proto_commands)


with open(os.path.join(file_dir, 'README.md')) as f:
    long_description = f.read()

install_requires = [
    'setuptools>=41.0.0',  # tensorboard requirements
    'tensorflow-gpu<2.0',
    'cython',
    'contextlib2',
    'pillow',
    'lxml',
    # replacement for pycocotools, as the published pypi package fails on cython and numpy dependencies
    'pycocotools-fix',
    'jupyter',
    'matplotlib'
]

setuptools.setup(
    name='tf_object_detection',
    version='0.0.3',
    author='Junjue Wang',
    author_email='junjuew@cs.cmu.edu',
    description='A Thin Wrapper around Tensorflow Object Detection API for Easy Installation and Use',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/junjuew/tf_object_detection',
    packages=setuptools.find_packages(
        where='tf_object_detection/research', include=['object_detection', 'object_detection.*']) + setuptools.find_packages(
        where='tf_object_detection/research/slim'),
    package_dir={
        '': 'tf_object_detection/research/slim',  # tf slim dependencies
        'object_detection': 'tf_object_detection/research/object_detection'},
    license='Apache License 2.0',
    install_requires=install_requires,
    python_requires='>3.5, <4',  # matplotlib >3.1 requires python >=3.6
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
    ]
)
