#!/usr/bin/env bash

hadoop jar ../hadoop-streaming-2.7.3.jar \
-D  mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
-D  mapreduce.map.output.field.seperator="." \
-D  mapreduce.partition.keycomparator.options="-k1,1n -k2,2n -k3,3" \
-D  num.key.fields.for.partition=1 \
-D  stream.num.map.output.key.field=3 \
-input ../uniLarge.txt \
-output output/ \
-mapper mapper.py \
-file mapper.py \
-reducer reducer.py \
-file reducer.py
