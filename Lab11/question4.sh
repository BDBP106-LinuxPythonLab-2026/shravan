#!/bin/bash
#> < operator, the comparison worked successfully. The shell basically interpreted that it should createa file called Nagesh due to the presence of the > symbol, hence the unwanted result.so using '\'in front of the operator compares without making a new file in the current dir.


val1=Jayashree
val2=Nagesh
if [ $val1 \> $val2 ]; then
echo "$val1 is greater than $val2"
else
echo "$val1 is lesser than $val2"
fi





