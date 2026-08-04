class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s_list=sorted(nums)
        return s_list[len(nums)//2]   #Majority element always at the middle

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         nums.sort()
#         the_middle = len(nums) // 2
#         return nums[the_middle]

# class Solution:
#     def majorityElement(self, nums):
#         n = len(nums)

#         for i in range(n):
#             count = 0

#             for j in range(n):
#                 if nums[i] == nums[j]:
#                     count += 1

#             if count > n // 2:
#                 return nums[i]



# class Solution:
#     def majorityElement(self, nums: list[int]) -> int:

#         element = None
#         count = 0 

#         for num in nums:
#             if count == 0:
#                 element = num
#             count += 1 if num == element else -1

#         return element  
