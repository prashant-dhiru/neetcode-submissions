class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_points = []
        
        for x, y in points:
            dist = (x**2) + (y**2)
            heapq.heappush(min_points, (-dist, x, y))
            if len(min_points) > k:
                heapq.heappop(min_points)
        
        return [[x,y] for (dist, x, y) in min_points ]

            