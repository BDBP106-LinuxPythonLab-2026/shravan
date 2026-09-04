#!/bin/bash

awk ' {print "Feed 1 "$1;}' |awk '{ "Feed 2 "$2}' | awk '{ "Feed 3 "$3  } ' | pig_weights.csv > pig_read.txt
