class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        res = 0 
        for num in nums:
            if num-1 in numbers:
                continue
            lcs = 0
            while num+lcs in numbers:
                lcs+=1
            res = max(res,lcs)
        return res