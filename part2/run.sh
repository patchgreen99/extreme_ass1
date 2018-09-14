#!/usr/bin/env bash

hadoop jar ../hadoop-streaming-2.7.3.jar -input ../part1/output -output output/ -mapper mapper.py -file mapper.py -reducer reducer.py -file reducer.py
