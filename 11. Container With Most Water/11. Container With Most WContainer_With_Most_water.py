class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        max_area=0
        while left<right:
            width = right-left 
            area= width * (min(height[left],height[right]))
            max_area=max(max_area,area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


# class Solution:
#     # Define the Solution class required by LeetCode

#     def maxArea(self, height: List[int]) -> int:
#         # Function that returns the maximum amount of water
#         # 'height' is a list containing the heights of vertical lines

#         left = 0
#         # Left pointer starts at the first line (index 0)

#         right = len(height) - 1
#         # Right pointer starts at the last line

#         max_area = 0
#         # Stores the largest area found so far
#         # Initially, no area has been calculated

#         while left < right:
#             # Continue until both pointers meet
#             # If left == right, width becomes 0, so no container exists

#             width = right - left
#             # Width of the container
#             # It is simply the distance between the two pointers

#             area = width * min(height[left], height[right])
#             # Calculate the current container's area
#             #
#             # Formula:
#             # Area = Width × Height
#             #
#             # Width = right - left
#             #
#             # Height is the SMALLER of the two lines because
#             # water cannot rise above the shorter line.
#             #
#             # Example:
#             # heights = [3, 7]
#             # Width = 1
#             # Height = min(3,7) = 3
#             # Area = 1 × 3 = 3

#             max_area = max(max_area, area)
#             # Compare the current area with the maximum area found so far
#             #
#             # If current area is larger,
#             # update max_area
#             #
#             # Otherwise,
#             # keep the previous maximum

#             if height[left] < height[right]:
#                 # If the left line is shorter

#                 left += 1
#                 # Move the left pointer one step to the right
#                 #
#                 # Why?
#                 # The shorter line limits the water level.
#                 # Moving the taller line inward cannot increase
#                 # the height of the container.
#                 # So we move the shorter one hoping to find
#                 # a taller line.

#             else:
#                 # Otherwise,
#                 # the right line is shorter
#                 # OR both lines are equal

#                 right -= 1
#                 # Move the right pointer one step to the left
#                 #
#                 # Again, we move the shorter side because
#                 # only replacing the shorter line can possibly
#                 # increase the area.

#         return max_area
#         # Return the maximum area found during the entire process
