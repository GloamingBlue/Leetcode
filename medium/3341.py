from typing import List
import heapq


class Solution:
  @staticmethod
  def minTimeToReach(moveTime: List[List[int]]) -> int:

    n = len(moveTime)
    m = len(moveTime[0])

    # min_arrival_times[r][c] 存储到达单元格 (r, c) 的最早时间
    # 初始化所有时间为无穷大
    min_arrival_times = [[float('inf')] * m for _ in range(n)]
    
    # 优先队列存储元组: (到达单元格的当前时间, 行, 列)
    # Python的heapq是最小堆，用于高效提取具有最小时间的单元格
    pq = []

    # 初始条件:
    # 你在时刻 t = 0 时从房间 (0, 0) 出发。这意味着到达 (0,0) 的时间是 0。
    # moveTime[r][c] (即 moveTime[r][c]) 的约束是关于“开始向这个房间移动”的。
    # 由于你初始就在 (0,0)，所以 moveTime[0][0] 不会延迟你在 t=0 时位于 (0,0) 这个事实。
    min_arrival_times[0][0] = 0
    heapq.heappush(pq, (0, 0, 0)) # (到达时间, 行, 列)

    # 定义四个方向的移动增量 (上, 下, 左, 右)
    delta_row = [-1, 1, 0, 0]
    delta_col = [0, 0, -1, 1]

    while pq:
        time_at_current_cell, r, c = heapq.heappop(pq)

        # 如果已经通过更短的路径访问过这个单元格，则跳过
        if time_at_current_cell > min_arrival_times[r][c]:
            continue

        # 如果到达了目标单元格 (n-1, m-1)
        if r == n - 1 and c == m - 1:
            return time_at_current_cell

        # 探索相邻单元格
        for i in range(4):
            nr, nc = r + delta_row[i], c + delta_col[i] # 相邻单元格的行和列

            # 检查相邻单元格是否在网格边界内
            if 0 <= nr < n and 0 <= nc < m:
                # time_at_current_cell 是到达当前单元格 (r,c) 的时间。
                # 理论上可以在 time_at_current_cell 时刻离开 (r,c)。
                # 对邻居 (nr,nc) 的移动时间约束是 moveTime[nr][nc]。
                # 必须在 moveTime[nr][nc] 或之后才能开始向 (nr,nc) 移动。
                
                # 因此，实际开始进行1秒移动的时刻是:
                time_to_initiate_move = max(time_at_current_cell, moveTime[nr][nc])
                
                # 到达相邻单元格 (nr,nc) 的时间是:
                arrival_time_at_neighbor = time_to_initiate_move + 1
                
                # 如果这条到达 (nr,nc) 的新路径比之前找到的任何路径都短
                if arrival_time_at_neighbor < min_arrival_times[nr][nc]:
                    min_arrival_times[nr][nc] = arrival_time_at_neighbor
                    heapq.heappush(pq, (arrival_time_at_neighbor, nr, nc))
    
    # 如果循环结束仍未返回，意味着目标无法到达。
    # 根据题目通常的结构，这种情况可能不会发生，或者会明确说明返回值。
    # 此处返回 -1 作为备选，但通常题目会保证可达性。
    return -1
        

if __name__ == '__main__':
    print(Solution.minTimeToReach([[0,4],[4,4]]))
    print(Solution.minTimeToReach([[0,0,0],[0,0,0]]))
