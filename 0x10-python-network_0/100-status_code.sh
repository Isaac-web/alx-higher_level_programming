#!/bin/bash
#prints the status code of a get request

curl -sI "$1" | grep HTTP | cut -d " " -f 2
