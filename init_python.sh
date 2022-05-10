#!/bin/zsh

MYPATH="/goinfre/$USER/miniconda3"
curl -LO "https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh"
sleep 1
sh Miniconda3-latest-Linux-x86_64.sh -b -p $MYPATH
sleep 1
$MYPATH/bin/conda init zsh 
$MYPATH/bin/conda init bash
$MYPATH/bin/conda config --set auto_activate_base false
source ~/.zshrc
source ~/.bashrc
sleep 1
echo "@creating conda environnement"
conda create --name 42AI-$USER python=3.7 jupyter pandas pycodestyle
echo "@Deleting Miniconda3"
rm Miniconda3-latest-linux-86_64.sh
conda activate 42AI-$USER
