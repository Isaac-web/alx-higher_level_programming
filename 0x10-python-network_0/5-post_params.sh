#!/bin/bash
#This script sends an http post request to the argument supplied
curl -sL -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
