class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0 
        
        l,r  = 0,0 
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = max(profit, prices[r]-prices[l])
            else:
                l = r
            r = r+1
            
        return profit