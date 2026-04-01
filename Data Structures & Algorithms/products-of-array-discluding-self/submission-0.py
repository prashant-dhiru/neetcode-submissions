class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        product = 1
        num_zero = 0
        for x in nums:
            if x == 0:
                num_zero += 1
            else:
                product *= x
        
        
        if num_zero == 1:
            for i,x in enumerate(nums):
                if x == 0:
                    ans[i] = product

        elif num_zero == 0:
            for i, x in enumerate(nums):
                ans[i] = product//x
            
        return ans
        