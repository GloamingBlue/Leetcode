from typing import List
from collections import defaultdict


class Solution:
    @staticmethod
    def longestPalindrome(words: List[str]) -> int:
        ans, flag = 0, 0  # ans代表的是结果中字符串的个数，flag是是否需要加1
        s = defaultdict(int)
        for word in words:
            s[word] += 1
        k = list(s.keys())  # 创建一个新的拷贝
        for w in k:
            if w == w[::-1]:  # 'aa'这种对称串
                if s[w] % 2 == 1:
                    flag = 1
                ans += (s[w] // 2) * 2  # 确保加入的是偶数
            else:
                ans += min(s[w], s[w[::-1]])  # 成对加入字符串
        return 2 * (ans + flag)


if __name__ == '__main__':
    print(f'{Solution.longestPalindrome(["lc", "cl", "gg"]) = }')
    print(f'{Solution.longestPalindrome(["ab", "ty", "yt", "lc", "cl", "ab"]) = }')
    print(f'{Solution.longestPalindrome(["cc", "ll", "xx"]) = }')
