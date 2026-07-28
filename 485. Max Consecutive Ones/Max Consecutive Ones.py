class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maximum = 0

        for num in nums:
            if num == 1:
                count += 1
            else:
                maximum = max(maximum, count)
                count = 0

        return max(maximum, count)


# #Brute force
# class Solution:
#     def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
#         n = len(nums)
#         maximum = 0

#         for i in range(n):

#             for j in range(i, n):

#                 if nums[j] == 0:
#                     maximum = max(maximum, j - i)
#                     break
#             else:
#                 # No zero found until the end
#                 maximum = max(maximum, n - i)

#         return maximum



# class Solution:
#     def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
#         curr = 0
#         max = 0
#         for x in nums:
#             if x ==1:
#                 curr += 1
#             else:
               
#                 if curr > max:
#                     max = curr
#                 curr = 0
                
                
                
#         if curr > max:
#             max = curr
#         return max
