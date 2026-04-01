# 0 2 0 3 1 0 1 3 2 1 
# 0 0 2 2 3 3 3 3 3 3
# 3 3 3 3 3 3 3 2 1 0
#------------------------ max((min - heights),0) 
# 0 0 2 0 2 3 2 0 0 0

class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0 

        while l < r:
            if leftMax < rightMax:
                l += 1
                res += max(leftMax - height[l], 0)
                leftMax = max(leftMax, height[l])
            else:
                r -= 1
                res += max(rightMax - height[r], 0)
                rightMax = max(rightMax, height[r])
        return res

