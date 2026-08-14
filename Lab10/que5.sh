#!/bin/bash
echo "enter marks (0-100)"
read num
if [ $num -le 100 ] && [ $num -ge 90 ]; then
echo 'GRADE "A"'
fi

if [ $num -le 89 ] && [ $num -ge 90 ]; then
 echo 'GRADE "B"'
fi


if [ $num -le 79 ] && [ $num -ge 70 ]; then
 echo 'GRADE "C"'
fi

if [ $num -le 60 ]; then
 echo 'GRADE "FAIL"'
fi



