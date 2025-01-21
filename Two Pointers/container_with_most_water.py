from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0  
        right = len(height) - 1 
        max_area = 0  
        highest = max(height)

        while left < right:

            #find smaller height of the pair
            if height[left] < height[right]:
                current_height = height[left]
            else:
                current_height = height[right]
            current_area = current_height * (right - left)
        
            #check for current area and max area
            if current_area > max_area:
                max_area = current_area
            if highest*(right-left) < max_area: #makes code efficient
                break
            
            #move our pointer
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area