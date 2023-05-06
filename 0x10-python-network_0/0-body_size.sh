#!/usr/bin/bash
#script that send request and display body size
curl -sI "$1" | grep -i Content-length | cut -d " " -f2
