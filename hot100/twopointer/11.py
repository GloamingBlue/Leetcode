from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = ans = 0
        right = len(height) - 1
        while left < right:
            ans = max(ans, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                cur = height[left]
                while height[left] <= cur and left < right:
                    left += 1
            else:
                cur = height[right]
                while height[right] <= cur and left < right:
                    right -= 1
        return ans
    

if __name__ == '__main__':
    print(f'{Solution().maxArea([1,8,6,2,5,4,8,3,7]) = }')
    print(f'{Solution().maxArea([1,1]) = }')
    print(f'{Solution().maxArea([1,1,1]) = }')
