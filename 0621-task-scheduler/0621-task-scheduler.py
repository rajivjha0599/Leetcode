class Solution:
     def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        counter = Counter(tasks)
        count = [-count for count in counter.values()]
        heapq.heapify(count)
        time = 0
        q = []
        while count or q:
            time+=1
            if count:
                maxHeap = heapq.heappop(count)+1
                if maxHeap:
                    q.append((maxHeap,time+n))

            if q and q[0][1] == time:
                heapq.heappush(count,q.pop(0)[0])
        return time