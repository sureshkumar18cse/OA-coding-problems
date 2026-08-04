class Solution:
    def maxProduct(self, nums):
        current_max = nums[0]
        current_min = nums[0]
        answer = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                current_max, current_min = current_min, current_max

            current_max = max(nums[i], current_max * nums[i])
            current_min = min(nums[i], current_min * nums[i])

            answer = max(answer, current_max)

        return answer


#Brute force approach failed for some cases
# class Solution: 
#     def maxProduct(self, nums):
#         n = len(nums)
#         maximum = nums[0]

#         for i in range(n):
#             product = 1

#             for j in range(i, n):
#                 product *= nums[j]

#                 maximum = max(maximum, product)

#         return maximum



# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         res = max(nums)
#         cur_max = cur_min = 1
#         for n in nums:
#             if n == 0:
#                 cur_max = cur_min = 1
#                 continue
#             tmp = cur_max * n
#             cur_max = max(n, cur_max * n, cur_min * n)
#             cur_min = min(n, tmp, cur_min * n)
#             res = max(res, cur_max)
#         return res
