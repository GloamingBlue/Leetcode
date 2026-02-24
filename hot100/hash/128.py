from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = 0
        m = len(nums)
        for i in nums:
            if i - 1 in nums:
                continue
            j = i + 1
            while j in nums:
                j += 1
            ans = max(ans, j - i)
            if ans * 2 >= m:
                break
        return ans
    

if __name__ == '__main__':
    print(Solution().longestConsecutive([100,4,200,1,3,2]))
    print(Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
    print(Solution().longestConsecutive([1,0,1,2]))
