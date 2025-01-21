from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left,count = 0,0
        right = len(nums)-1
        while left < right:
            if  nums[left] + nums[right] == k: 
                right -= 1
                count += 1
                left += 1
            elif nums[left] + nums[right] > k:
                right -= 1
            else:
                left += 1

        return count