from typing import List
from collections import defaultdict


class Solution:
    @staticmethod
    def numRabbits(answers: List[int]) -> int:
        ans = 0
        cnt = defaultdict(int)
        for a in answers:
            cnt[a + 1] += 1
        for key in cnt.keys():
            ans += (cnt[key] + key-1) // key * key  # 向上取整
        return ans


if __name__ == '__main__':
    print(Solution.numRabbits([10, 10, 10]))
