#!/usr/bin/python3
#Oct 10, 2026
#Question11
"""Write a program to concatenate a list of strings to make a sentence using reduce function."""
from functools import reduce

L = ["afasg", "argge", "arggergerg", "rgergregerg"]
sentence = reduce(lambda a, b: a + " " + b, L)
print(sentence)
concat = reduce(lambda a, b: a + b, L)
print(concat)