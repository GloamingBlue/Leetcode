from typing import List


class Solution:
    @staticmethod
    def buildArray(nums: List[int]) -> List[int]:
        n = len(nums)
        mask = (1 << 10) - 1  # 要加括号，因为移位运算符优先级低；构建掩码，这样能得到低位的结果，因为nums[i]的取值范围是0-999，所以右移10位就够了(0-1023)
        for i in range(n):
            nums[i] |= (nums[nums[i]] & mask) << 10
        for i in range(n):
            nums[i] >>= 10
        return nums


if __name__ == '__main__':
    print(Solution.buildArray([0, 2, 1, 5, 3, 4]))
