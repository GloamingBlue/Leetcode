from typing import List
from collections import defaultdict


class Solution:
    @staticmethod
    def lengthAfterTransformations(s: str, t: int, nums: List[int]) -> int:
        cnt = defaultdict(list)  # 预处理得到字符映射关系
        for i in range(26):
            for j in range(1, nums[i] + 1):
                cnt[(i + j) % 26].append(i)
        dp = [[0] * 26 for _ in range(t)]  # dp数组，dp[i]为第i次迭代得到的每个字母的数量


if __name__ == '__main__':
    Solution.lengthAfterTransformations("abcyy", 2, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2])
