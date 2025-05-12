from collections import defaultdict


MOD = 1000000007


class Solution:
    @staticmethod
    def lengthAfterTransformations(s: str, t: int) -> int:
        cnt = defaultdict(int)
        for c in s:
            cnt[c] += 1
        ans = 0



