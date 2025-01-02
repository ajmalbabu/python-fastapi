# setting up VS code, manual step is better
# install python3 via home brew or via direct installation from python website 
# another options is to follow the below VS code link, but did not work
https://code.visualstudio.com/docs/python/python-tutorial#__install-a-python-interpreter

# code clone the code from ajmalbabu github, the original code from arjan is below
https://github.com/ArjanCodes/2023-fastapi

# setup virtual env with command: Follow this manual step by going to the source code download folder
python3 -m venv .venv
source .venv/bin/activate
# or via VS code step, manual is better
https://code.visualstudio.com/docs/python/python-tutorial#_create-a-virtual-environment

# Once the above is done, make sure by clicking on any python file the latest python version is showed in the status bar

# To run below in the app at terminal execute following: instead put them in request.txt file 
pip3 install fastapi
pip3 install uvicorn
pip3 install requests

# in terminal run below
uvicorn app:app --reload


# follow video for this project: 
https://www.youtube.com/watch?v=SORiTsvnU28


# Alternte to above is to use 'gunicorn' which can help with concurreny and also setup cloud loadbalancer correctly

# check if the application is running coorectly with http methods
http://127.0.0.1:8000/docs or http://127.0.0.1:8000/redoc

# hit browser: 
http://127.0.0.1:8000/


# Read: virtual env, fastapi and testing: 
https://code.visualstudio.com/docs/python/python-tutorial#_create-a-virtual-environment

