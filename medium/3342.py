from typing import List
from numpy import inf
import heapq


class Solution:
    @staticmethod
    def minTimeToReach(moveTime: List[List[int]]) -> int:
        
        q = [(0, 0, 0)]  # 最小堆
        n, m = len(moveTime), len(moveTime[0])
        minArrival = [[inf] * m for _ in range(n)]  # 维护房间的最早访问时间，出发点的值没有用到，可以不做修改

        while q:
            timeArr, x, y = heapq.heappop(q)
            if x == n-1 and y == m-1:
                return timeArr
            if timeArr > minArrival[x][y]:
                continue
            for nx, ny in (x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1):
                if -1 < nx < n and -1 < ny < m:
                    newArrival = max(timeArr, moveTime[nx][ny]) + (x + y) % 2 + 1
                    if newArrival < minArrival[nx][ny]:
                        minArrival[nx][ny] = newArrival
                        heapq.heappush(q, (newArrival, nx, ny))
        return -1
    

if __name__ == '__main__':
    print(Solution.minTimeToReach([[0, 0, 0, 0], [0, 0, 0, 0]]))
    print(Solution.minTimeToReach([[0, 4], [4, 4]]))
