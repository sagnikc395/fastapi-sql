#!/bin/bash 

## danger -> will kill any service working on the port to start the FASTAPI service  
sudo lsof -t -i tcp:8080 | xargs kill -9
