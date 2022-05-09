#!/bin/bash

# install required packages

pip install pip
pip install setuptools
pip install wheel
pip install build

python3 -m build

pip install dist/my_minipack-1.0.0.tar.gz
