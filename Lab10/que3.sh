#!?bin/bash
echo 'Enter file name:'
read file

if [ -f "$file" ]; then 
echo 'file exists'
	if [ -x "$file" ]; then
	echo 'file is executable'
	else
	echo 'file not executable'
	exit 201
	echo #?
	fi
else 
echo 'file does not exists'
exit 200
echo #?
fi

echo 'outside the if block' exit 0
