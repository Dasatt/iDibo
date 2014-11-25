__author__ = 'satope'
"""Pig Latin is a language game, where you move the first letter of the word to the end and add "ay."
 So "Python" becomes "ythonpay."""

print "Welcome to Pig Latin Translator!"

original = raw_input("Enter an English word: ")

pyg = "ay"

#Ensure user inputs something and also a full text no numbers or special characters
if len(original) != 0 and original.isalpha():
    print original
    word = original.lower()
    first = word[0]
    new_word = word + first + pyg
    print new_word
else:
    print "Empty"
