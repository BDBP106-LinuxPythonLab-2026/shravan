#!/usr/bin/python3
#25 sep, 2026
#question5
"""Remove all duplicate words from a given sentence using a dictionary. (Hint: Use the
set() function might be useful here.)"""
sentence="Rain Rain go away come again another day, do not come again today"
words=sentence.split()
dict_words={}
final=[]
for word in words:
    if word in dict_words:
        pass
    else:
        dict_words[word]=1
        final.append(word)
print('The unique list of words are: ',dict_words)
print('The sentence now is "',' '.join(final),'"')