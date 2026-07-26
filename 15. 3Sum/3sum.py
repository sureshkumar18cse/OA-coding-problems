class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()          # Step 1: Sort the array
        result = []
        n = len(nums)

        for i in range(n - 2):

            # Skip duplicate fixed numbers
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:

                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1

                elif total > 0:
                    right -= 1

                else:
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicate left values
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicate right values
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return result

# class Solution:  #Issue Time limit exceed so not optimal code this one (Brute Force)
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         ans = []
#         n = len(nums)

#         for i in range(n):
#             for j in range(i + 1, n):
#                 for k in range(j + 1, n):

#                     if nums[i] + nums[j] + nums[k] == 0:
#                         triplet = sorted([nums[i], nums[j], nums[k]])

#                         if triplet not in ans:
#                             ans.append(triplet)

#         return ans

