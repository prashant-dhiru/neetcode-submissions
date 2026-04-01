class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        largeElement = []
        for num in nums:
            heapq.heappush(largeElement, num)
            if len(largeElement) > k:
                heapq.heappop(largeElement)
            # print(largeElement)

        return largeElement[0]
            