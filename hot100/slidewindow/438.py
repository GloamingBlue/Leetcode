from typing import List
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:  # 考察counter的用法，包括使用==判断两个counter是否相等，使用滑动窗口枚举窗口左端点
        ans = []
        a, b = len(s), len(p)
        cntP = Counter(p)
        for i in range(a - b + 1):
            if Counter(s[i:i+b]) == cntP:
                ans.append(i)
        return ans
    
    def answer(self, s: str, p: str) -> List[int]:  # 灵神的题解，枚举右端点，而且特判左端点小于0的时候进行初始化
        ans = []
        l = len(p)
        cntP = Counter(p)
        cnt = Counter()  # 用于更新窗口端点的计数
        for right, a in enumerate(s):
            cnt[a] += 1
            left = right - l + 1  # 左端点位置
            if left < 0:
                continue
            if cnt == cntP:
                ans.append(left)
            cnt[s[left]] -= 1
        return ans


if __name__ == '__main__':
    print(f'{Solution().findAnagrams("cbaebabacd", "abc") = }')
    print(f'{Solution().findAnagrams("abab", "ab") = }')
    print(f'{Solution().answer("cbaebabacd", "abc") = }')
    print(f'{Solution().answer("abab", "ab") = }')