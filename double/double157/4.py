from typing import List
from collections import deque

MOD = 1_000_000_007


class Solution:
    @staticmethod
    def assignEdgeWeights(edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = len(edges) + 1  # 节点总数
        # 构建邻接表
        adj = [[] for _ in range(n + 1)]  # adj[0] 不使用，节点编号从1开始
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # 预处理深度和父节点信息（使用 BFS）
        parent = [0] * (n + 1)  # parent[u] 是 u 的父节点
        depth = [0] * (n + 1)  # depth[u] 是 u 的深度（到根的距离）
        visited = [False] * (n + 1)

        q = deque([1])  # 从根节点1开始
        visited[1] = True

        while q:
            u = q.popleft()
            for v in adj[u]:
                if not visited[v] and v != parent[u]:
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    visited[v] = True
                    q.append(v)

        # 倍增法预处理每个节点的 2^k 级祖先
        MAX_LOG = 20  # 对于 n <= 1e6 的树，20足够
        up = [[0] * (n + 1) for _ in range(MAX_LOG)]

        # up[k][u] 表示 u 的 2^k 级祖先
        for u in range(1, n + 1):
            up[0][u] = parent[u]  # 2^0 = 1，即直接父节点

        # 递推计算 up 数组
        for k in range(1, MAX_LOG):
            for u in range(1, n + 1):
                up[k][u] = up[k - 1][up[k - 1][u]]

        # LCA 查询函数
        def lca(x, y):
            # 确保 u 的深度 >= v 的深度
            if depth[x] < depth[y]:
                x, y = y, x

            # 将 u 提升到与 v 相同的深度
            for i in range(MAX_LOG - 1, -1, -1):
                if depth[x] - (1 << i) >= depth[y]:
                    x = up[i][x]

            # 如果此时 u == v，说明 v 是 u 和 v 的 LCA
            if x == y:
                return x

            # 同时提升 u 和 v，找到它们的 LCA
            for i in range(MAX_LOG - 1, -1, -1):
                if up[i][x] != up[i][y]:
                    x = up[i][x]
                    y = up[i][y]

            # 此时 u 和 v 的父节点即为 LCA
            return parent[x]

        # 计算两节点间的路径长度
        def get_path_length(x, y):
            ancestor = lca(x, y)
            return depth[x] + depth[y] - 2 * depth[ancestor]

        return [2 ** (get_path_length(a, b) - 1) % MOD if a != b else 0 for a, b in queries]


if __name__ == '__main__':
    print(f'{Solution.assignEdgeWeights([[1, 2]], [[1, 1], [1, 2]]) = }')
    print(f'{Solution.assignEdgeWeights([[1, 2], [1, 3], [3, 4], [3, 5]], [[1, 4], [3, 4], [2, 5]]) = }')
