from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:  # 模拟或者找规律
        dirList = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 方向数组
        dir = 0  # 方向:0代表向右,1代表向下,2代表向左,3代表向上,满足顺时针要求且和方向数组对应
        ans = []
        m, n = len(matrix), len(matrix[0])
        i, j = 0, -1  # 设置起始位置
        size = m * n
        while len(ans) < size:
            for _ in range(n):
                i, j = i+dirList[dir][0], j+dirList[dir][1]
                ans.append(matrix[i][j])
            dir = (dir + 1) % 4
            n, m = m - 1, n
        return ans
    
if __name__ == '__main__':
    print(f'{Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]]) = }')
    print(f'{Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) = }')
