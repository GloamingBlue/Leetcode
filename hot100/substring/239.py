from typing import List
from collections import deque


class solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * (len(nums) - k + 1)
        q = deque()
        for i, j in enumerate(nums):
            while q and nums[q[-1]] <= j:
                q.pop()
            q.append(i)
            left = i + 1 - k
            if q[0] < left:
                q.popleft()
            if left >= 0:
                ans[left] = nums[q[0]]
        return ans
    

if __name__ == '__main__':
    print(f'{solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3) = }')
    print(f'{solution().maxSlidingWindow([1], 1) = }')
    print(f'{solution().maxSlidingWindow([3,1,1,3], 3) = }')

