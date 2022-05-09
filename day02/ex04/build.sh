#!/bin/bash

# install required packages

pip install --upgrade pip
pip install --upgrade setuptools
pip install --upgrade wheel
pip install --upgrade build

python3 -m build

pip install dist/my_minipack-1.0.0.tar.gz
