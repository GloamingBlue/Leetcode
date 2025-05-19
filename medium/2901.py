from typing import List


class Solution:
    @staticmethod
    def getWordsInLongestSubsequence(words: List[str], groups: List[int]) -> List[str]:
        def hanMing(a: str, b: str) -> bool:
            """判断两个字符串的汉明距离是否为1"""
            return len(a) == len(b) and sum(r != s for r, s in zip(a, b)) == 1
        
        n = len(words)
        dp, idx = [0] * n, [0] * n  # 初始化最长子序列数组和下表记录数组
        maxIdx = n - 1  # 初始化最长子序列下标
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if dp[j] <= dp[i] or groups[j] == groups[i] or not hanMing(words[j], words[i]):
                    continue
                dp[i] = dp[j]
                idx[i] = j  # 更新索引
            dp[i] += 1
            if dp[i] > dp[maxIdx]:  # 如果出现了更长的子序列，更新maxIdx
                maxIdx = i
        
        ans = []
        m = dp[maxIdx]
        for i in range(m):
            ans.append(words[maxIdx])
            maxIdx = idx[maxIdx]
        return ans


if __name__ == '__main__':
    print(f'{sum([True, False, True, False]) = }')
    print(f'{Solution.getWordsInLongestSubsequence(["bab", "dab", "cab"], [1, 2, 2]) = }')
    print(f'{Solution.getWordsInLongestSubsequence(["a", "b", "c", "d"], [1, 2, 3, 4]) = }')
