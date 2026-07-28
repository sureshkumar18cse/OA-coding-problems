class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        left_max = height[left]
        right_max = height[right]

        water = 0

        while left < right:

            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                water += left_max - height[left]

            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += right_max - height[right]

        return water   

# class Solution:
#     def trap(self, height):
#         left = 0
#         right = len(height) - 1

#         left_max = 0
#         right_max = 0

#         water = 0

#         while left < right:

#             if height[left] < height[right]:

#                 if height[left] >= left_max:
#                     left_max = height[left]
#                 else:
#                     water += left_max - height[left]

#                 left += 1

#             else:

#                 if height[right] >= right_max:
#                     right_max = height[right]
#                 else:
#                     water += right_max - height[right]

#                 right -= 1

#         return water








# # Algorithm - brute force gets time exceed

# # For every position

# # Find tallest on left

# # Find tallest on right

# # Take minimum

# # Subtract current height

# # Add answer

# class Solution:
#     def trap(self, height):
#         n = len(height)
#         water = 0

#         for i in range(n):

#             left_max = 0
#             right_max = 0

#             # Find tallest wall on left
#             for j in range(i + 1):
#                 left_max = max(left_max, height[j])

#             # Find tallest wall on right
#             for j in range(i, n):
#                 right_max = max(right_max, height[j])

#             water += min(left_max, right_max) - height[i]

#         return water
