#!/bin/bash

echo $0

echo 'The first argument: ',$1
echo 'the second argument: ',$2

echo 'the number of arguments passed in the script : ' $#
echo 'the array list of arguments passed in the script: '$@

# We can store the arguments in an array by enclosing $@ within ()  
listofarg=($@)
#Recall elements like any other array
echo ${listofarg[*]}

