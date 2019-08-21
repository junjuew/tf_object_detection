import glob
import os
import shutil

import setuptools

file_dir = os.path.dirname(os.path.realpath(__file__))


def _copy_pb2_files():
    """Copy compiled protobuf files into the python package for distribution."""
    dest_dir = os.path.join(
        file_dir, 'tf_object_detection/research/object_detection/protos/')
    for filename in glob.glob(os.path.join(file_dir, 'pb2', '*.*')):
        shutil.copy(filename, dest_dir)


_copy_pb2_files()


with open(os.path.join(file_dir, 'README.md')) as f:
    long_description = f.read()

install_requires = [
    'tensorflow-gpu<2.0',
    'numpy',  # explicitly declared as pycocotools does not declare it explicitly
    'cython',
    'contextlib2',
    'pillow',
    'lxml',
    'pycocotools',
    'jupyter',
    'matplotlib'
]

setup_requires = [
    'setuptools>=18.0',
    'cython',
    'numpy'
]

setuptools.setup(
    name='tf_object_detection',
    version='0.0.2.4',
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
    setup_requires=setup_requires,
    python_requires='>3.4, <4',
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
    ]
)
