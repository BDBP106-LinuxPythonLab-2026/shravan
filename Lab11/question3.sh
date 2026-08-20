#!/bin/bash

str="12-10"

if [ -n $str ]; then
	echo "string exists"
else 
	echo "string doesnot exist"
fi

str1="12*0"
if [ -z $str1 ]; then
	echo "string not equal to 0"
else 
	echo "string is empty"
fi

