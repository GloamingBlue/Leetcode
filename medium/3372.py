from typing import List
from collections import deque


class Solution:
    @staticmethod
    def maxTargetNodes(edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        def radius(edges: List[List[int]], m: int) -> List[int]:
            """求树中某点在半径k内的邻接点的个数"""
            n = len(edges) + 1
            g = [[] for _ in range(n)]
            res = [0] * n
            if m < 0:  # 如果k==0则k-1==-1导致m<0，只能返回0
                return res
            for a, b in edges:
                g[a].append(b)
                g[b].append(a)
            for i in range(n):
                d = deque([i])
                s = {i}
                for _ in range(m):
                    tmp = [d.popleft() for _ in range(len(d))]  # 清空队列
                    d.extend([y for x in tmp for y in g[x] if y not in s])  # 更新队列
                    s.update(list(d))  # 更新集合
                res[i] = len(s)
            return res

        radi1 = radius(edges1, k)
        return list(map(lambda x: x + max(radius(edges2, k - 1)), radi1))


if __name__ == '__main__':
    print(f'{Solution.maxTargetNodes([[0, 1], [0, 2], [2, 3], [2, 4]], [[0, 1], [0, 2], [0, 3], [2, 7], [1, 4], [4, 5], [4, 6]], 2) = }')
    print(f'{Solution.maxTargetNodes([[0, 1], [0, 2], [0, 3], [0, 4]], [[0, 1], [1, 2], [2, 3]], 1) = }')
