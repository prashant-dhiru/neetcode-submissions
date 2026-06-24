class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # ans = [0] * 2 * n

        # for i, x in enumerate(nums):
        #     ans[i] = nums[i]
        #     ans[i + n] = nums[i]
        nums.extend(nums)
        return nums
