#!/usr/bin/env bash

hadoop jar ../hadoop-streaming-2.7.3.jar -input ../webLarge.txt -output output/ -mapper mapper.py -file mapper.py
