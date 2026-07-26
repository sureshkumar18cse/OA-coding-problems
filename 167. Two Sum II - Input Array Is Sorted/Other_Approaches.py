# Yes. There are several approaches, but only one satisfies all the problem constraints. Let's go through them from beginner to optimal.

# Approach 1: Brute Force (Nested Loops)
# Idea

# Check every pair of numbers.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        n = len(numbers)

        for i in range(n):
            for j in range(i + 1, n):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
# Example
# numbers = [2,7,11,15]
# target = 9

# Check

# 2 + 7 = 9 ✓

# Return

# [1,2]
# Complexity
# Time: O(n²)
# Space: O(1)

# ✅ Constant space

# ❌ Too slow for large inputs.

# Approach 2: Hash Map (Dictionary)

# This is the solution for the original Two Sum problem (unsorted array).

# Idea

# Store each number in a dictionary.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        seen = {}

        for i, num in enumerate(numbers):

            complement = target - num

            if complement in seen:
                return [seen[complement] + 1, i + 1]

            seen[num] = i
# Example
# numbers = [2,7,11,15]
# target = 9

# Iteration 1

# seen = {}

# num = 2

# need = 7

# 7 not found

# store

# seen = {2:0}

# Iteration 2

# num = 7

# need = 2

# 2 exists

# return [1,2]
# Complexity
# Time: O(n)
# Space: O(n)

# ❌ The problem specifically says constant extra space, so this is not allowed.

# Approach 3: Binary Search

# Since the array is sorted, for every element we can binary search for its complement.

# Code
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        n = len(numbers)

        for i in range(n):

            need = target - numbers[i]

            left = i + 1
            right = n - 1

            while left <= right:

                mid = (left + right) // 2

                if numbers[mid] == need:
                    return [i + 1, mid + 1]

                elif numbers[mid] < need:
                    left = mid + 1

                else:
                    right = mid - 1
# Example
# numbers = [2,7,11,15]

# target = 9

# Take

# 2

# Need

# 7

# Binary search

# 7 11 15

# Find

# 7

# Return

# [1,2]
# Complexity
# Time: O(n log n)
# Space: O(1)

# ✅ Constant space

# ❌ Slower than two pointers.

# Approach 4: Two Pointers (Optimal)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers) - 1

        while left < right:

            s = numbers[left] + numbers[right]

            if s == target:
                return [left + 1, right + 1]

            elif s < target:
                left += 1

            else:
                right -= 1
# Complexity
# Time: O(n)
# Space: O(1)

# ✅ Fastest

# ✅ Uses constant space

# Comparison
# Approach	Time	Space	Uses Sorted Array?	Meets Problem Requirement?
# Brute Force	O(n²)	O(1)	No	✅ Yes
# Hash Map	O(n)	O(n)	No	❌ No (extra space)
# Binary Search	O(n log n)	O(1)	✅ Yes	✅ Yes
# Two Pointers	O(n)	O(1)	✅ Yes	✅ Best
