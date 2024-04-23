echo [${date}]: "START"

echo [${date}]: "Creating env with python 3.8 version"

conda create --prefix ./env python=3.8 -y

echo [$(date)]: "activating the environment"

source activate ./env

echo [$(date)]: "installing the dev requirement"

pip install -r requirements.txt

echo [$(date)]: "End"