#!/bin/bash
function maximum {
	n1=$1
	n2=$2
	if [ $n1 -gt $n2 ]; then
		echo "$n1 is greater"
	else
		echo "$n2 is greater"
	fi
}
maximum 67 90
