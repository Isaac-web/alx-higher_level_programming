#!/bin/bash
#This script sends a delete request to the end point provided
curl "$1" -X DELETE -s
