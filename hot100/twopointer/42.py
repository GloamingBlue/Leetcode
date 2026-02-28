from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # 三种做法：1.前后缀分解 2.相向双指针 3.单调栈. 这里给出双指针做法，本质和前后缀等价
        ans = 0
        n = len(height)
        l, r = 0, n-1
        preMax, sufMax = 0, 0
        while l < r:
            preMax = max(preMax, height[l])
            sufMax = max(sufMax, height[r])
            if preMax < sufMax:
                ans += preMax - height[l]
                l += 1
            else:
                ans += sufMax - height[r]
                r -= 1
        return ans
    

if __name__ == '__main__':
    print(f'{Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]) = }')
    print(f'{Solution().trap([4,2,0,3,2,5]) = }')
    print(f'{Solution().trap([3,5]) = }')
    print(f'{Solution().trap([3]) = }')
