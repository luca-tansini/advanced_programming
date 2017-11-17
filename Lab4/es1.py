#To extend the class for the strings to support the following operations:

    #-to check if the string is palindrome, a string is palindrome when the represented sentence can be read the same way in either directions in spite of spaces, punctual and letter cases, e.g., detartrated, "Do geese see God?", "Rise to vote, sir.", ...
    #-to subtract the letters in a string from the letters in another string, e.g., "Walter Cazzola"-"abcwxyz" will give "Wlter Col" note that the operator - is case sensitive and that the target should be a name containing an instance of the child class
    #-given a dictionary of strings, to check if the string is an anagram of one or more of the strings in the dictionary

import re

class MyString(str):

    def trimPunctuation(self):
        return re.sub('[.,;:\'\"?!() ]','',self)

    def palindrome(self):
        s = self.trimPunctuation().lower()
        return s == s[len(s)::-1]

    def __sub__(self,other):
        pattern = ""
        for c in set(other): pattern += c
        pattern = re.sub("[\]\[]",'/\g<0>',pattern).replace("/","\\")
        pattern = "[" + pattern + "]"
        return re.sub(pattern,'',self)

    def isanagram(self,strings):
        for s in strings:
            if(sorted(list(self))==sorted(list(s))): return True
        return False
