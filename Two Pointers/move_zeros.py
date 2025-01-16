from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_pos = 0

        for i in range(len(nums)):
            if(nums[i]!=0):
                nums[zero_pos] = nums[i]
                zero_pos += 1

        while(zero_pos < len(nums)):
            nums[zero_pos] = 0
            zero_pos += 1

if __name__ == "__main__":
    ob = Solution()

    nums = [0, 1, 0, 3, 12]

    print(ob.moveZeroes(nums))