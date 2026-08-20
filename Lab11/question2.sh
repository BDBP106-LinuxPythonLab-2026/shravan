#!/bin.bash
# -e shows if the files are present or not
# -s looks if the file is empty or not empty
# -f looks for a regular file

# -e shows if the files are present or not
# -s looks if the file is empty or not empty
# -f looks for a regular file

# -e shows if the files are present or not
# -s looks if the file is empty or not empty
# -f looks for a regular file


if [ -e listoffiles ]; then 
	echo "file exists"
else 
	echo "file doesnot exist"
fi

if [ -s q2blank ]; then 
	echo "file exists with contents"
else 
	echo "file exist empty"
fi

if [ -f q2blank ]; then 
	echo "file"
else 
	echo "not a regular file"
fi
