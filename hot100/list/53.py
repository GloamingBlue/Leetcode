from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        s = minSub = 0
        for i in nums:
            s += i
            ans = max(ans, s - minSub)
            minSub = min(minSub, s)
        return ans
    

if __name__ == '__main__':
    print(f'{Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) = }')
    print(f'{Solution().maxSubArray([1]) = }')
    print(f'{Solution().maxSubArray([5,4,-1,7,8]) = }')
