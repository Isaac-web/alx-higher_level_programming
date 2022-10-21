#!/bin/bash
#sends a get request to a url along with a header
curl -sL -H "X-School-User-Id: 98" "$1"
