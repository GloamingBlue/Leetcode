from typing import List
from itertools import accumulate


class Solution:
    @staticmethod
    def isZeroArray(nums: List[int], queries: List[List[int]]) -> bool:
        diff = [0] * (len(nums) + 1)  # 防止右侧越界
        for l, r in queries:
            diff[l] += 1
            diff[r + 1] -= 1
        for x, y in zip(nums, accumulate(diff)):
            if x > y:
                return False
        else:
            return True


if __name__ == '__main__':
    print(f'{Solution.isZeroArray([1, 0, 1], [[0, 2]]) = }')
    print(f'{Solution.isZeroArray([4, 3, 2, 1], [[1, 3], [0, 2]]) = }')
