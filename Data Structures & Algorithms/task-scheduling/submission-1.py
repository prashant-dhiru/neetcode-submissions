class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # each task is 1 unit of time
        # minimize idle time

        count = Counter(tasks)
        maxHeap = [-num for num in count.values()]
        heapq.heapify(maxHeap)

        time = 0 
        q = deque() # pair of [-num, idealTime]

        while maxHeap or q:
            time += 1
            if maxHeap:
                num = 1 + heapq.heappop(maxHeap)
                if num:
                    q.append([num, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time
