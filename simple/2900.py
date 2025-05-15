from typing import List


class Solution:
    @staticmethod
    def getLongestSubsequence(words: List[str], groups: List[int]) -> List[str]:
        ans = [words[0]]
        t = groups[0]

        for i, v in enumerate(groups[1:]):
            if v ^ t:
                ans.append(words[i + 1])
                t = v
        return ans


if __name__ == '__main__':
    print(Solution.getLongestSubsequence(["e",  "a", "b"], [0, 0, 1]))
    print(Solution.getLongestSubsequence(["a", "b", "c", "d"], [1, 0, 1, 1]))
