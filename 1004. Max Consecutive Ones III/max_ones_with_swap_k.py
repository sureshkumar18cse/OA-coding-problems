class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zeros = 0
        maximum = 0

        for right in range(len(nums)):

            if nums[right] == 0:
                zeros += 1

            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1

                left += 1

            maximum = max(maximum, right - left + 1)

        return maximum




#           EXPAND
#              ↓
# left ─────────────── right
#        valid window

#              ↓
#       too many zeros?

#              ↓ YES

# left ──→ ──→ ──→ right
#      SHRINK

#              ↓
#       zeros <= k

#              ↓
#        calculate length

# left = 0
# count = 0
# answer = 0

# for right in range(len(nums)):

#     # Add right element
#     if nums[right] == 0:
#         count += 1

#     # Window invalid
#     while count > k:

#         if nums[left] == 0:
#             count -= 1

#         left += 1

#     # Window valid
#     answer = max(answer, right - left + 1)

# return answer

# class Solution:  #Brute force failed with large input size
#     def longestOnes(self, nums: List[int], k: int) -> int:
#         n = len(nums)
#         maximum = 0

#         for i in range(n):
#             zeros = 0

#             for j in range(i, n):

#                 if nums[j] == 0:
#                     zeros += 1

#                 if zeros > k:
#                     break

#                 maximum = max(maximum, j - i + 1)

#         return maximum
