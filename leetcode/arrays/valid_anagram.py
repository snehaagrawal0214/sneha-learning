# Placeholder for Valid Anagram solution
# Problem: Valid Anagram
# Difficulty: Easy
# Pattern: Arrays + Hashing
# Date: 29 Jun 2026
# Time complexity: O(n) - where n is the length of the strings (since we are iterating through both strings once to build the frequency dictionaries).
# Space complexity: O(1) - since the size of the hashmap is limited to the number of unique characters in the alphabet (which is constant).

# My approach: store the frequency of each characters in hashmap and compare the two hash for both string.
# if equal then return true or false.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # Create a frequency dictionary for the first string
        freq_s = {}
        for char in s:
            freq_s[char] = freq_s.get(char, 0) + 1

        # Create a frequency dictionary for the second string
        freq_t = {}
        for char in t:
            freq_t[char] = freq_t.get(char, 0) + 1

        # Compare the two frequency dictionaries
        return freq_s == freq_t
    
# from collections import Counter

# freq_s = Counter(s)  # One line! {'a': 2, 'b': 1} for "aab"
# freq_t = Counter(t)  # One line! {'a': 2, 'b': 1} for "aab"
# return freq_s == freq_t



# what I learned:
# 1. Using a hashmap (dictionary in Python) allows for efficient counting of character frequencies
# 2. The time complexity of this solution is O(n) because we are iterating through both strings once to build the frequency dictionaries, and the space complexity is O(1) because the size of the hashmap is limited to the number of unique characters in the alphabet (which is constant).
# 3. The Counter class from the collections module can simplify the frequency counting process, making the code more concise and readable.