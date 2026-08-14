#1/bin/bash
echo "enter a number"
read num

if [ $num -lt 0 ]; then
echo "the number is negative"
elif [ $num -gt 0 ]; then
echo "then number is positive"
else 
echo "the number is zero"
fi

