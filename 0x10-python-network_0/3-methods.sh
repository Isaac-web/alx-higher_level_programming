#!/bin/bash
#This script prints the  methods that are accepted on a url

curl -sL "$1" | grep Allow | cut -d " " -f 2-
