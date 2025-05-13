from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def countPairs(nums: List[int], k: int) -> int:
        ans = 0
        cnt = defaultdict(list)
        num = set(nums)
        for i, j in enumerate(nums):
            cnt[j].append(i)
        for a in num:
            b = cnt.get(a)
            length = len(b)
            if length == 1:
                continue
            for i, c in enumerate(b):
                for j in range(i + 1, length):
                    if c * b[j] % k == 0:
                        ans += 1
        return ans


if __name__ == '__main__':
    ans =  Solution.countPairs([3,1,2,2,2,1,3], 2)
    print(ans)
