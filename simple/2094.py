from typing import List
from collections import defaultdict


class Solution:
    @staticmethod
    def findEvenNumbers(digits: List[int]) -> List[int]:
        """暴力枚举"""
        ans = []
        cnt = defaultdict(int)
        for num in digits:
            cnt[num] += 1
        nums = sorted(cnt.keys())
        for k in nums:
            if k:
                for j in nums:
                    for i in nums:
                        if not i % 2:
                            if k != j and j != i and i!= k:  # 三个数不等
                                ans.append(100 * k + 10 * j + i)
                            elif k == j and j == i:  # 三个数相等
                                if cnt[i] >2:
                                    ans.append(100 * k + 10 * j + i)
                            else:  # 有两个数相等
                                if k == j and cnt[k] > 1:
                                    ans.append(100 * k + 10 * j + i)
                                elif k == i and cnt[k] > 1:
                                    ans.append(100 * k + 10 * j + i)
                                elif i == j and cnt[i] > 1:
                                    ans.append(100 * k + 10 * j + i)
        return ans

    @staticmethod
    def findEvenNumbers1(digits: List[int]) -> List[int]:
        """回溯"""
        ans = []
        cnt = defaultdict(int)
        for num in digits:
            cnt[num] += 1
        nums = sorted(cnt.keys())

        def dfs(i: int, d : int):
            if i == 3:  # 加入合法的结果
                ans.append(d)
                return
            for num in nums:
                if cnt[num] > 0 and ((i == 0 and num >0) or i == 1 or (i == 2 and not num % 2)):
                    cnt[num] -= 1
                    dfs(i + 1, num + 10 * d)
                    cnt[num] += 1
        
        dfs(0, 0)
        return ans


if __name__ == '__main__':
    print(Solution.findEvenNumbers([2,1,3,0]))
    print(Solution.findEvenNumbers1([2,1,3,0]))
