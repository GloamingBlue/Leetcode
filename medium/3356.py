from typing import List
from itertools import accumulate


class Solution:
    @staticmethod
    def minZeroArray(nums: List[int], queries: List[List[int]]) -> int:
        def check(k: int) -> bool:
            """检查前k个查询是否得到零数组"""
            diff = [0] * (len(nums) + 1)
            for l, r, val in queries[:k]:
                diff[l] += val
                diff[r + 1] -= val
            for a, b in zip(nums, accumulate(diff)):
                if a > b:
                    return False
            else:
                return True

        length = len(queries)
        left, right = -1, length + 1  # 开区间二分查找
        while left + 1 < right:  # 开区间判断条件
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid
        return right if right < length + 1 else -1  # -1代表无法得到，0到length代表能得到


if __name__ == '__main__':
    print(Solution.minZeroArray([2, 0, 2], [[0, 2, 1], [0, 2, 1], [1, 1, 3]]))
    print(Solution.minZeroArray([4, 3, 2, 1], [[1, 3, 2], [0, 2, 1]]))
