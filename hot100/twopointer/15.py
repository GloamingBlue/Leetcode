from typing import List
from collections import defaultdict


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        numSet = defaultdict(list)
        for i, j in enumerate(nums):
            numSet[j].append(i)
        numKey = set(nums)
        for i in numKey:
            for j in numKey:
                if -i-j in numKey:
                    if i != j and j != -i-j and -i-j != i:
                        if (i, j, -i-j) not in ans and (i, -i-j, j) not in ans and (j, i, -i-j) not in ans and (j, -i-j, i) not in ans and (-i-j, i, j) not in ans and (-i-j, j, i) not in ans:
                            ans.add((i, j, -i-j))
                    elif i == j == -i-j:
                        if len(numSet[0]) > 2:
                            ans.add((0, 0, 0))
                    elif i == j:
                        if len(numSet[i]) > 1 and (i, i, -i-j) not in ans:
                            ans.add((i, i, -i-j))
                    elif j == -i-j:
                        if len(numSet[j]) > 1 and (j, j, i) not in ans:
                            ans.add((j, j, i))
                    else:
                        if len(numSet[i]) > 1 and (i, i, j) not in ans:
                            ans.add((i, i, j))
        return [list(t) for t in ans]

    def threeSumAnswer(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            x = nums[i]
            if x + nums[i+1] + nums[i+2] > 0:
                break
            if x + nums[-2] + nums[-1] < 0:
                continue
            j, k = i + 1, n - 1
            while j < k:
                s = x + nums[j] + nums[k]
                if s < 0:
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    j += 1
                elif s > 0:
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    k -= 1
                else:
                    ans.append([x, nums[j], nums[k]])
                    print(i,j,k)
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    k -= 1
        return ans


if __name__ == '__main__':
    print(f'{Solution().threeSum([-1,0,1,2,-1,-4]) = }')
    print(f'{Solution().threeSum([0,1,1]) = }')
    print(f'{Solution().threeSum([0,0,0]) = }')
    print(f'{Solution().threeSumAnswer([-1,0,1,2,-1,-4]) = }')
    print(f'{Solution().threeSumAnswer([2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]) = }')
    print(f'{Solution().threeSumAnswer([0,0,0]) = }')
    print(f'{Solution().threeSumAnswer([0,0,0,0]) = }')
