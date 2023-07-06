#!/bin/bash
#script that send request and display body size
curl -s "$1" | wc -c
