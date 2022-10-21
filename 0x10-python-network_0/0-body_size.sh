#!/bin/bash
# This script takes a url and returns the length of the body
curl "$1" -sL | wc -c
