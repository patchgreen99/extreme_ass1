#!/usr/bin/env bash

hadoop jar ../hadoop-streaming-2.7.3.jar \
-D  mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
-D  mapreduce.map.output.field.seperator=. \
-D  num.key.fields.for.partition=2 \
-D  mapreduce.partition.keypartitioner.options=-k1 \
-input ../part4/output \
-output output/ \
-mapper mapper.py \
-file mapper.py \
-reducer reducer.py \
-file reducer.py


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