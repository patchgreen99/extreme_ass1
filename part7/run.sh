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

#-D  mapreduce.map.input.field.seperator="\t" \
#-D  num.key.fields.for.comparator=3 \


#-D  mapred.input.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
#-D  mapreduce.map.input.field.seperator=. \
#-D  num.key.fields.for.partition=2 \
#-D  mapreduce.partition.keypartitioner.options=-k1 \

#-reducer reducer.py \
#-file reducer.py


#-D  num.key.fields.for.partition=3 \
#-D  num.key.fields.for.comparator=3 \
#-D  stream.num.map.input.key.field=3 \

#-D  mapred.input.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
#-D  mapreduce.partition.keypartitioner.options=-k1,1 \
#-D  mapreduce.partition.keycomparator.options=-k1,1nr \
#-D  stream.num.map.input.key.field=1 \


#-reducer 'head -n 20'


#-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner
#-D  mapred.input.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
#-D  stream.map.input.field.seperator=\t \
#-D  stream.num.map.input.key.field=2 \
#-D  mapreduce.partition.keycomparator.options=-k2nr \
#-D  mapred.reduce.tasks=1 \

#-partitioner
#-D  mapred.input.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
#-D  stream.num.map.input.key.field=4 \
#-D  mapreduce.partition.keycomparator.options=-k4nr \
#-D  stream.map.input.field.seperator= \