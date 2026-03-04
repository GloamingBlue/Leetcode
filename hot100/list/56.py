from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort(key=lambda x : x[0])  # 按照列表元素的第1维度排序
        for i in intervals:
            if ans and i[0] <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], i[1])
            else:
                ans.append(i)
        return ans
    

if __name__ == '__main__':
    print(f'{Solution().merge([[1,3],[2,6],[8,10],[15,18]]) = }')
    print(f'{Solution().merge([[1,4],[4,5]]) = }')
    print(f'{Solution().merge([[4,7],[1,4]]) = }')
