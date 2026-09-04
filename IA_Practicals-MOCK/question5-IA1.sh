#!/bin/bash

function arguments {
	echo 'Argument 1: '$1
	echo 'Argument 2: '$2
	echo 'Argument 3: '$3
	echo 'Argument 4: '$4
}

var=$#
arguments $1 $2 $3 $4
echo "total number of arguments; " $var
 exit $var
