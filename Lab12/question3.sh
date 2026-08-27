#!/bin/bash

echo "Enter a number"
read n
echo "Enter a number"
i=1
until [ $i -gt 15 ]
do 
	echo "$n * $i = $(( n * i ))"
	i=$[i+1]
done

