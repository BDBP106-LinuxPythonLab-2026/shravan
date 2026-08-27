#!/bin/bash
n=50
for (( i=1 ; i<=$n ; i++))
do
	if [ $((i % 2 )) -eq 0 ]; then
	echo $i
	fi
done	
