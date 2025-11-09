#!/usr/bin/env bash
#locate the shell dir
letter1=$(echo $0 |cut -c1-1)
if [ $letter1 = "/" ] ; then
    APP_DIR=$(dirname $0)
else
    APP_DIR=$(pwd)/$(dirname $0)
fi

cd $APP_DIR

python3="/c/Users/Administrator/AppData/Local/Programs/Python/Python310/python"

export PATH="/c/Users/Administrator/AppData/Local/Programs/Python/Python310:$PATH"

if [ ! -e ".venv" ] ; then
$python3 -m venv .venv
fi


source .venv/Scripts/activate &&\
pip install -r requirements.txt

source .venv/Scripts/activate &&\
python setup.py install


source .venv/Scripts/activate &&\
cd $APP_DIR &&\
python ./src/mcp_atlassian/__init__.py

