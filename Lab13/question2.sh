#!/bin/bash

#(i)
awk ' $2<25  {print "the people names who are scored less than 25 in their subjects are " $1} ' awk.txt

#(ii)
awk ' $3=="Physics" {print "Student whose physics marks are given is " $1}' awk.txt

#(iii)
awk '{print $1"," $2 "," $3}' awk.txt > data.csv


