from typing import List
from collections import deque


class Solution:
    @staticmethod
    def maxCandies(status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]],
                   initialBoxes: List[int]) -> int:
        l1, tempBox = [], []  # 后者暂存已得到但无钥匙的箱子
        for a in initialBoxes:
            if status[a]:
                l1.append(a)
            else:
                tempBox.append(a)
        d = deque(l1)  # 已得到已打开未处理的箱子
        ans = 0

        while d:
            b = d.popleft()
            ans += candies[b]  # 结算糖果数
            for k in keys[b]:  # 根据钥匙更新可打开的箱子
                status[k] = 1
            for t in tempBox[:]:  # 查找已得到的箱子是否有可打开的
                if status[t]:
                    tempBox.remove(t)  # 对数组遍历时删除当前的遍历元素是否安全?会的，所以遍历时使用切片
                    d.append(t)
            for cont in containedBoxes[b]:  # 对新得到的箱子进行分类
                if status[cont]:
                    d.append(cont)
                else:
                    tempBox.append(cont)

        return ans


if __name__ == '__main__':
    print(f'{Solution().maxCandies([1, 0, 1, 0], [7, 5, 4, 100], [[], [], [1], []], 
                                   [[1, 2], [3], [], []], [0]) = }')
    print(f'{Solution().maxCandies([1, 1, 1], [100, 1, 100], [[], [0, 2], []], 
                                   [[], [], []], [1]) = }')
    print(f'{Solution().maxCandies([1], [100], [[]], [[]], []) = }')
    print(f'{Solution().maxCandies([1, 1, 1], [2, 3, 2], [[], [], []], [[], [], []], 
                                   [2, 1, 0]) = }')
