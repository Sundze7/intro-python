#!/bin/bash 

HOME=$(pwd)
PY_VERSION=$(python3 -V 2>&1 | cut -d' ' -f2)
PY_MAJOR=${PY_VERSION%%.*}
PY_MINOR=${PY_VERSION#*.}
PY_MINOR=${PY_MINOR%.*}

# Verify if a virtual env folder exists
if [ ! -d "myenv" ]; then
    echo "Create a python virtual environment called 'venv'"
    exit 1 
fi 

if ! which zip; then 
    # Install zip if it's not installed
    echo "Installing zip..."
    sudo apt install zip -y

    # verify it it's installed.
    if ! which zip; then
        echo "zip installation failed. Exiting"
        exit 1 
    fi 
fi 
echo "zip is installed"

if [ -d packages ]; then 
    rm -r packages/
fi 

PACKAGE_PATH=packages/python/lib/python${PY_MAJOR}.${PY_MINOR}/site-packages
# Create the packages directory
mkdir -p $PACKAGE_PATH
cp -r myenv/lib/python*/site-packages/* $PACKAGE_PATH

cd packages
zip -r ../packages.zip .
cd ..
rm -r packages/
echo ""
echo "packages.zip file created"

zip function.zip *.py 

echo ""
echo "functions.zip file created"
echo "Function Python version ${PY_MAJOR}.${PY_MINOR}"