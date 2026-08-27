#!/bin/bash

function file {
	echo "Enter a filename"
	read f
	if  [ -e $f ];then
		echo "File exists"
		ls $f	  
	else
		mkdir newdirectory
		echo "New directory is created"

	fi
}
file
