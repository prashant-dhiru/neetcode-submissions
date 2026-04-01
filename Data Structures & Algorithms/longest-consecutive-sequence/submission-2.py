class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        res = 0 
        for num in nums:
            if num-1 in numbers:
                continue
            ss = num
            lcs = 0
            while ss in numbers:
                lcs+=1
                ss+=1
            res = max(res,lcs)
        return res