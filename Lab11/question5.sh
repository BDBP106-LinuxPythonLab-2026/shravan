val1=Testing
val2=testing
if [ $val1 \> $val2 ]; then
echo "$val1 is greater than $val2"
else
echo "$val1 is lesser than $val2"
fi

#result Testing is greater than testing

echo "$val2 $val1" >> teststringfile
sort teststringfile
