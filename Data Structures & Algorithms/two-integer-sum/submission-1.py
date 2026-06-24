class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} #num, index
        for i,num in enumerate(nums):
            if target-num in seen:
                return [seen.get(target-num), i]
            seen.update({num:i})
        return [-1,-1]