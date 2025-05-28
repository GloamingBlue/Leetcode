from typing import List
from collections import defaultdict


class Solution:
    @staticmethod
    def largestPathValue(colors: str, edges: List[List[int]]) -> int:
        """三色标记法查找是否有环，结合记忆化搜索"""
        n = len(colors)
        # 初始化邻接表
        g = [[] for _ in range(n)]
        for a, b in edges:
            if a == b:  # 自环
                return -1
            g[a].append(b)

        memo = [None for _ in range(n)]  # 记忆化数组，存储节点的状态（0代表在栈中）以及dfs的返回值

        def dfs(i: int) -> defaultdict or int:
            if memo[i] is not None:  # 当前节点被访问过且已经递归完成，直接返回上次递归的值；当前节点入栈且未返回（标记为0）,返回0，有环
                return memo[i]
            memo[i] = 0  # 代表正在访问中
            res = defaultdict(int)
            for j in g[i]:  # 访问邻接点
                tempJ = dfs(j)
                if not tempJ:  # 有环,tempJ==0
                    return tempJ
                for k, v in tempJ.items():
                    res[k] = max(res[k], v)
            res[colors[i]] += 1
            memo[i] = res
            return res

        ans = 0
        for idx, c in enumerate(colors):
            t = dfs(idx)
            if not t:
                return -1
            ans = max(ans, t[c])
        return ans


if __name__ == '__main__':
    print(f'{Solution.largestPathValue("abaca", [[0, 1], [0, 2], [2, 3], [3, 4]]) = }')
    print(f'{Solution.largestPathValue("a", [[0, 0]]) = }')
