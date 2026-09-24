#!/usr/bin/python3
#24 sept, 2026
#question9
"""a script to check if two strings are anagrams of each other . Eg. listen and silent are anagrams, gram and arm are not anagrams"""
word1=input("enter a sentence: ")
word2=input("enter second sentence: ")
if sorted(word1) == sorted(word2):
	print("it is anagram")
else:
	print("not anagrams")

