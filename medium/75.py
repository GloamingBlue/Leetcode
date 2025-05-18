from typing import List


class Solution:
    @staticmethod
    def sortColors(nums: List[int]) -> None:
        p, q = 0, 0  # p、q分别代表0的个数、0和1的总数
        for i, x in enumerate(nums):  # 这里i即代表已插入的0、1、2的总数，x为当前需要插入的数
            nums[i] = 2  # 覆盖插入
            if x <= 1:
                nums[q] = 1
                q += 1
            if x == 0:
                nums[p] = 0
                p += 1
    

if __name__ == '__main__':
    Solution.sortColors([2, 0, 2, 1, 1, 0])
