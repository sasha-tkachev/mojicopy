#!/bin/sh
repo_root=$( dirname -- "$0"; )
cd $repo_root
dist_dir="./dist"
mkdir $dist_dir -p 
rm -rf $dist_dir
python setup.py sdist
python setup.py bdist_wheel
cd $dist_dir
twine upload *