# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 14:10:42 2022

@author: Okhrimchuk Roman
for Sierentz Global Merchants


Test task
"""
# TODO Import the necessary libraries


# TODO Write here is_palindrome function


def is_palindrome(x):
    x = str(x)
    backwords = x[::-1]
    backwords = backwords.replace(' ', '').replace("?", '').replace('&', "1")
    x = x.replace(' ', '').replace("?", '').replace('&', "1")
    x = x.lower()
    backwords = backwords.lower()

    if x == backwords:
        return True

    else:
        return False


print(is_palindrome(""))
print(is_palindrome(1010))
print(is_palindrome("taco Cat"))
print(is_palindrome("Was it a car or a cat I saw?"))
print(is_palindrome("hello"))
print(is_palindrome("momma made me eat my m&ms"))
