# heap fragmentation
A lightweight Stackoverflow clone, a website where users can ask for advice and other users can post their answers
![image](https://user-images.githubusercontent.com/102432364/180626546-3f0c99d4-ebd6-4bb2-a71a-ac4a4aea5057.png)

# demo
[Demo](http://147.182.220.50:8000/)

# install
These are Linux installation instructions.

1. Install [pip (pip3) for Python 3](https://linuxize.com/post/how-to-install-pip-on-ubuntu-18.04/)
2. Install Django

```
python -m pip install Django
```
```
pip install Django==3.2.7
```

# run
Firstly change directory to `advice/advice`. Then start the Django server: 
```
python3 manage.py runserver --insecure {IP address}:8000 &
```
where `{IP address}` is the public IP address of your Django server. 

