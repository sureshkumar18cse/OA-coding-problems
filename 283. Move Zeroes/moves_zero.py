class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        
        return nums
# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         l=0
#         for r in range(len(nums)):
#             if nums[r]!=0:
#                 temp = nums[r]
#                 nums[r]=nums[l]
#                 nums[l]=temp
#                 l+=1


# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         n = []
#         c = 0

#         for i in range(len(nums)):
#             if nums[i] == 0:
#                 c += 1
#             else:
#                 n.append(nums[i])

#         nums[:] = n + [0] * c

