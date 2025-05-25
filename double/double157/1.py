import math


class Solution:
    @staticmethod
    def sumOfLargestPrimes(s: str) -> int:
        a = set()

        def check(num: str) -> bool:
            """判断是否为质数"""
            if num == 2 or num == 3:
                return True
            for i in range(2, round(math.sqrt(num)) + 1):
                if num % i == 0:
                    return False
            else:
                return True

        for j in range(len(s)):
            for k in range(0, j + 1):
                n = int(s[k:j+1])
                if n > 1 and check(n):
                    a.add(int(s[k:j+1]))
        a = sorted(a)
        return sum(a[-3:]) if len(a) >= 3 else sum(a)


if __name__ == '__main__':
    print(f'{Solution.sumOfLargestPrimes(s="12234") = }')
    print(f'{Solution.sumOfLargestPrimes(s="111") = }')
    print(f'{Solution.sumOfLargestPrimes(s="2") = }')
