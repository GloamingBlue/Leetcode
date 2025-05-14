from typing import List
from collections import defaultdict


MOD = 1_000_000_007


class Solution:
    @staticmethod
    def lengthAfterTransformations(s: str, t: int, nums: List[int]) -> int:
        cnt = defaultdict(list)  # 预处理得到字符映射关系
        for i in range(26):
            for j in range(1, nums[i] + 1):
                cnt[(i + j) % 26].append(i)
        dp = [[0] * 26, [0] * 26]  # dp数组，dp[0]为第偶数次迭代得到的每个字母的数量/dp[1]为第奇数次迭代得到的每个字母的数量
        for c in s:  # 初始化原字符串的字母个数
            dp[0][ord(c) - 97] += 1
        
        for i in range(1, t + 1):
            idx1, idx2 = i % 2, i % 2 - 1
            dp[idx1] = [0] * 26  # 清零上一次存储的数组
            for j in range(26):
                for k in cnt[j]:
                    dp[idx1][j] = (dp[idx1][j] + dp[idx2][k]) % MOD
        return sum(dp[t % 2]) % MOD


if __name__ == '__main__':
    print(Solution.lengthAfterTransformations("abcyy", 2, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]))
    print(Solution.lengthAfterTransformations("azbk", 1, [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]))
