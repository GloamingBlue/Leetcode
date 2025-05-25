class Solution:
    @staticmethod
    def minCuttingCost(n: int, m: int, k: int) -> int:
        if n <= k and m <= k:
            return 0
        elif n > k and m <= k:
            return (n - k) * k
        elif m > k and n <= k:
            return (m - k) * k
        else:
            return (n - k) * k + (m - k) * k


if __name__ == '__main__':
    print(f'{Solution.minCuttingCost(n = 6, m = 5, k = 5) = }')
    print(f'{Solution.minCuttingCost(n = 4, m = 4, k = 6) = }')
