class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        zero_count = 0

        for num in nums:
            if num == 0: zero_count += 1
            else : total_product *= num
        res = [0] * len(nums)
        if zero_count == 1 :
            for i,num in enumerate(nums):
                if num == 0: res[i]=total_product
        elif zero_count == 0 :
            for i,num in enumerate(nums):
                res[i] = total_product // nums[i]
        return res