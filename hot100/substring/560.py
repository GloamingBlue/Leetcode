from typing import List
from collections import defaultdict


class solution:
    def subarraySum(self, nums: List[int], k: int):
        ans = s = 0
        cnt = defaultdict(int)
        cnt[0] = 1
        for num in nums:
            s += num
            ans += cnt[s - k]
            cnt[s] += 1
        return ans
    

if __name__ == '__main__':
    print(f'{solution().subarraySum([1,1,1], 2) = }')
    print(f'{solution().subarraySum([1,2,3], 3) = }')
