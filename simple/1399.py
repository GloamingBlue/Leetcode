from collections import defaultdict


class Solution:
    @staticmethod
    def countLargestGroup(n: int) -> int:
        cnt = defaultdict(int)
        for x in range(1, n+1):
            idx = sum(map(int, str(x)))
            cnt[idx] += 1
        max_value = max(cnt.values())
        return sum(1 if val == max_value else 0 for val in cnt.values())


if __name__ == '__main__':
    print(Solution.countLargestGroup(24))
