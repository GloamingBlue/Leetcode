from typing import List


class Solution:
    @staticmethod
    def triangleType(nums: List[int]) -> str:
        nums.sort()
        if nums[0] + nums[1] <= nums[2]:
            return 'none'
        else:
            if nums[0] == nums[2]:
                return 'equilateral'
            elif nums[0] == nums[1] or nums[1] == nums[2]:
                return 'isosceles'
            else:
                return 'scalene'


if __name__ == '__main__':
    print(Solution().triangleType([3, 3, 3]))
    print(Solution().triangleType([3, 4, 5]))
