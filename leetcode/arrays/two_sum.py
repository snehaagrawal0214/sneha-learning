# Placeholder for Two Sum solution
# Problem: Two Sum
# Difficulty: Easy
# Pattern: Arrays + Hashing
# URL: https://leetcode.com/problems/two-sum/
# Date: 28 Jun 2026
# Time complexity: O(n)
# Space complexity: O(n)

# My approach:
# Use a hashmap to store complement values. --> this will allow us to check if the complement exists in O(1) time.
# enumerate is used to get the index of the current number in the list.
# enumerate(nums) gives us both the index and the value of each number in the list.
# For each number, check if its complement exists in the map.


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        if len(nums) < 2:
            return []
        # hashmap to store the index of each number
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []
    


#what I learned:
# The key idea is to remember numbers that have already been seen. When the code looks at a new number, it checks whether the complement for that number is already stored in the dictionary. If it is, the two matching indices are returned immediately. If not, the current number and its index are saved so they can be used later. This makes the search efficient because checking whether a value exists in a dictionary is very fast.
# 1. Using a hashmap (dictionary in Python) allows for efficient lookups of the previously seen numbers so that we can quickly find their matching pattern.
# 2. The hashmap stores the number as the key and its index as the value.
# 3 # enumerate(nums) gives (index, value) pairs in one pass — use it whenever you need both, avoids range(len(nums)).
# 4. The time complexity of this solution is O(n) because we are iterating through the list once, and the space complexity is also O(n) because we are storing the indices of the numbers in a hashmap.


if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    result = sol.twoSum([2, 7, 11, 15], 9)
    print(f"Test 1: nums=[2,7,11,15], target=9 → {result}")
    assert result == [0, 1], f"Expected [0, 1], got {result}"

    # Test case 2
    result = sol.twoSum([3, 2, 4], 6)
    print(f"Test 2: nums=[3,2,4], target=6 → {result}")
    assert result == [1, 2], f"Expected [1, 2], got {result}"

    # Test case 3 (edge case)
    result = sol.twoSum([1], 1)
    print(f"Test 3: nums=[1], target=1 (edge case) → {result}")
    assert result == [], f"Expected [], got {result}"

    print("\n All tests passed!")