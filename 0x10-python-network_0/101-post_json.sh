#!/bin/bash
#Sends an http request to an api end point
curl -sL -H "Content-Type: application/json" X POST -d "@$2" "$1"
