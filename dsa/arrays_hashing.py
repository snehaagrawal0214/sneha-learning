# Pattern: Arrays + Hashing
#
# CORE IDEA:
# Trade O(n) extra space for O(1) lookup speed.
# Use a dict/set to remember values seen so far → when you need to check if
# something exists, you find it instantly instead of scanning the whole array again.
#
# TIME & SPACE TRADEOFF:
# - Brute force (no hashing): O(n²) time, O(1) space (just loops)
# - With hashing: O(n) time, O(n) space (one loop + dict)
#
# HOW IT WORKS (Two Sum example):
# Problem: Given nums=[2,7,11,15], target=9, return indices of two numbers that sum to target
#
# Step 1: As you iterate through the array, store each number in a dict
#         dict format: {number: index}
#         Example: seen = {2: 0, 7: 1}
#
# Step 2: For each new number, check: does my COMPLEMENT exist in the dict already?
#         Complement = target - current_number
#         Example: For 7, complement = 9 - 7 = 2. Is 2 in seen? Yes! Return [0, 1]
#
# KEY PYTHON TOOLS FOR THIS PATTERN:
# dict       → store key:value pairs, O(1) lookup/insert
# set        → store just values for existence checks, O(1) lookup/insert
# enumerate  → get (index, value) pairs in one loop, cleaner than range(len())
#
# OTHER PROBLEMS USING THIS PATTERN:
# Contains Duplicate  → set existence check (is this number already seen?)
# Valid Anagram       → dict frequency count (do both words have same char counts?)
# Group Anagrams      → dict with sorted chars as key (group anagrams together)
# Top K Frequent      → Counter (frequency dict) + heap (get top K)