# setting up VS code 
https://code.visualstudio.com/docs/python/python-tutorial#__install-a-python-interpreter

# setup virtual env with command: Follow this link 
https://code.visualstudio.com/docs/python/python-tutorial#_create-a-virtual-environment

# follow video for this project: 
https://www.youtube.com/watch?v=SORiTsvnU28

# code base
https://github.com/ArjanCodes/2023-fastapi

# To run below in the app at terminal execute following: instead put them in request.txt file 
pip3 install fastapi
pip3 install uvicorn
pip3 install requests

# in terminal run below
uvicorn app:app --reload

# Alternte to above is to use 'gunicorn' which can help with concurreny and also setup cloud loadbalancer correctly

# check if the application is running coorectly with http methods
http://127.0.0.1:8000/docs or http://127.0.0.1:8000/redoc

# hit browser: 
http://127.0.0.1:8000/


# Read: virtual env, fastapi and testing: 
https://code.visualstudio.com/docs/python/python-tutorial#_create-a-virtual-environment

