class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers) - 1

        while left < right:

            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return [left + 1, right + 1]

            elif current_sum < target:
                left += 1

            else:
                right -= 1



               
# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         l=0
#         r=len(numbers)-1
#         while l<r:
#             su = numbers[l]+numbers[r]
#             if su==target :
#                 return [l+1,r+1]
#             if su<target:
#                 l+=1
#             if su>target:
#                 r-=1
