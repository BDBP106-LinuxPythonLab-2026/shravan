#/bin/bash

#(i)
sed -n '/and/p' Python.txt

#(ii)
sed 's/language/lang/g' Python.txt

#(iii)
sed '/is/d' Python.txt

#(iv)
sed = Python.txt | sed 'N;s/\n/ /'

#(v)
sed '1,2d' Python.txt

#(vi)
sed -n '1-2p' Python.txt

#(vii)
 sed 's/Python/python/g;s/language/lang/g' Python.txt


