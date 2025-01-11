class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        ans = [0] * n
        
        # Count zeros and calculate product of non-zero numbers
        zero_count = 0
        total_product = 1
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                total_product *= num
        
        # If more than one zero, all products will be 0
        if zero_count > 1:
            return ans
            
        # If exactly one zero, only its position will be non-zero
        if zero_count == 1:
            for i in range(n):
                if nums[i] == 0:
                    ans[i] = total_product
            return ans
            
        # If no zeros, divide total product by each number
        for i in range(n):
            ans[i] = total_product // nums[i]
            
        return ans