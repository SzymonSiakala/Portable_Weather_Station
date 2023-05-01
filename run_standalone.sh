#!/bin/bash
sudo docker pull szymsia398/standalone_app
sudo docker run -ti --privileged -d -p 5000:5000 -ti --mount type=bind,source="/home/raspberry"/data,target=/data szymsia398/standalone_app