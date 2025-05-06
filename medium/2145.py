from typing import List
from itertools import accumulate


class Solution:
    @staticmethod
    def numberOfArrays(differences: List[int], lower: int, upper: int) -> int:
        differences = list(accumulate(differences, initial=0))
        return max(upper - lower - max(differences) + min(differences) + 1, 0)
    

if __name__ == '__main__':
    print(Solution.numberOfArrays([3, -4, 5, 1, -2], -4, 5))
