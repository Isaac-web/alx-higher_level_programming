#!/bin/bash
#This script sends a delete request to a 
#url passed as an arguement

curl "$1" -X DELETE -s
