# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         curr = nums[0]
#         ma = nums[0]
#         for i in range(1,len(nums)):
#             curr=max(nums[i],curr+nums[i])
#             ma=max(ma,curr)
#         return ma
        

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = max_sum = nums[0]

        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)

        return max_sum       


#return that subarray also
      
# class Solution:
#     def maxSubArray(self, nums: List[int]):
#         curr_sum = nums[0]
#         max_sum = nums[0]

#         start = 0
#         left = 0
#         right = 0

#         for i in range(1, len(nums)):
#             if nums[i] > curr_sum + nums[i]:
#                 curr_sum = nums[i]
#                 start = i
#             else:
#                 curr_sum += nums[i]

#             if curr_sum > max_sum:
#                 max_sum = curr_sum
#                 left = start
#                 right = i

#         return max_sum, nums[left:right+1]
