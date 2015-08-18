#!/usr/bin/env python
# Exercise 3  
# (1) Write a function called most_frequent that takes a string and prints the
#     chars in decreasing order of frequency. (compare and print in lowercase)
# Ex. >>> most_frequent("aaAbcc")
#     a  
#     c
#     b
###############################################################################
# Imports

import string

# Body

def most_frequent(s):
    d = dict()
    inv = dict()
    for char in s:
        if char in string.ascii_letters:
            letter = char.lower()       
            d[letter] = d.get(letter, 0) + 1
            
    for letter, freq in d.items():
        inv.setdefault(freq, []).append(letter)
        
    for freq in sorted(inv, reverse=True):
        print(inv[freq])

###############################################################################
def main():   # DO NOT CHANGE BELOW
    print("Example 1:")
    most_frequent("abcdefghijklmnopqrstuvwxyz")
    print("\nExample 2:")
    most_frequent("The quick brown fox jumps over the lazy dog")
    print("\nExample 3:")
    most_frequent("Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
    "sed do eiusmod tempor incididunt ut labore et dolore magna "
    "aliqua. Ut enim ad minim veniam, quis nostrud exercitation "
    "ullamco laboris nisi ut aliquip ex ea commodo consequat. "
    "uis aute irure dolor in reprehenderit in voluptate velit "
    "esse cillum dolore eu fugiat nulla pariatur. Excepteur sint "
    "occaecat cupidatat non proident, sunt in culpa qui officia "
    "deserunt mollit anim id est laborum.")
    print("\nExample 4:")
    most_frequent("Squdgy fez, blank jimp crwth vox!")

if __name__ == '__main__':
    main()
