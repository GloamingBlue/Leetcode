from bisect import bisect_right, bisect_left
from typing import List


class Solution:
    @staticmethod
    def countFairPairs(nums: List[int], lower: int, upper: int) -> int:
        ans = 0
        if lower > upper:
            return ans
        nums.sort()  # 排序并不会改变总数目，因此后面可以进行二分查找确定数量
        for j, x in enumerate(nums):
            ans += bisect_right(nums, upper - x, 0, j) - bisect_left(nums, lower - x, 0, j)
        return ans


if __name__ == '__main__':
    print(Solution().countFairPairs(nums=[1, 7, 9, 2, 5], lower=11, upper=11))
