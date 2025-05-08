from typing import List
import heapq


class Solution:
    @staticmethod
    def minTimeToReach(moveTime: List[List[int]]) -> int:
        q = []  # 最小堆
        n, m = len(moveTime), len(moveTime[0])
        minArrival = [[float('inf')] * m for _ in range(n)]  # 维护房间的最早访问时间
        direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # 上下左右四个方向
        heapq.heappush(q, (0, 0, 0, 1))
        while q:
            timeArr, i, j, num = heapq.heappop(q)
            if i == n-1 and j == m-1:
                    return timeArr
            for x, y in direction:
                nx, ny = i + x, j + y
                if -1 < nx < n and -1 < ny < m: 
                    newArrival = max(timeArr + 2 - num % 2, moveTime[nx][ny] + 2 - num % 2)
                    if newArrival < minArrival[nx][ny]:
                        minArrival[nx][ny] = newArrival
                        heapq.heappush(q, (minArrival[nx][ny], nx, ny, num + 1))
        return -1
    

if __name__ == '__main__':
    print(Solution.minTimeToReach([[0, 0, 0, 0], [0, 0, 0, 0]]))
    print(Solution.minTimeToReach([[0, 4], [4, 4]]))
