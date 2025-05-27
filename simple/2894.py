class Solution:
    @staticmethod
    def differenceOfSums(n: int, m: int) -> int:
        return n * (n + 1) // 2 - (n // m) * (1 + n // m) * m


if __name__ == '__main__':
    print(f'{Solution.differenceOfSums(10, 3) = }')
    print(f'{Solution.differenceOfSums(5, 6) = }')
    print(f'{Solution.differenceOfSums(5, 1) = }')
