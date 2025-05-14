from typing import List
from collections import defaultdict


MOD = 1_000_000_007


class Solution:
    @staticmethod
    def lengthAfterTransformations(s: str, t: int, nums: List[int]) -> int:
        """暴力模拟，会超时"""
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

    @staticmethod
    def lengthAfterTransformations1(s: str, t: int, nums: List[int]) -> int:
        """使用矩阵快速幂优化的动态规划"""
        m = [[0] * 26 for _ in range(26)]  # 字母变换矩阵
        for i in range(26):  # 初始化变换矩阵
            for j in range(1, nums[i] + 1):
                m[i][(i + j) % 26] = 1
        cnt = [[0] * 26]  # 得到字符串中字母个数
        for c in s:
            cnt[0][ord(c) - 97] += 1

        return Solution.matrixMul(cnt, Solution.quickMatrixPow(m, t))[0][0]

    @staticmethod
    def matrixMul(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        """实现矩阵乘法a@b，并对中间结果取模"""
        return [[sum(x * y for x, y in zip(row, col)) % MOD for col in zip(*b)] for row in a]

    @staticmethod
    def quickMatrixPow(a: List[List[int]], n: int) -> List[List[int]]:
        """实现矩阵快速幂，并将最终结果乘以单位列向量"""
        f0 = [[1] for _ in range(len(a))]
        while n:
            if n & 1:
                f0 = Solution.matrixMul(a, f0)
            a = Solution.matrixMul(a, a)
            n >>= 1
        return f0


if __name__ == '__main__':
    print(Solution.lengthAfterTransformations("abcyy", 2, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]))
    print(Solution.lengthAfterTransformations("azbk", 1, [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]))
    print(Solution.lengthAfterTransformations1("abcyy", 2, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]))
    print(Solution.lengthAfterTransformations1("azbk", 1, [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]))
