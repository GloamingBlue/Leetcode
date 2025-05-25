class Solution:
    @staticmethod
    def maxSubstrings(word: str) -> int:
        n = len(word)
        if n < 4:
            return 0
        i, j, ans = 0, 1, 0

        while j < n:
            if j > i + 2 and word[j] in word[i:j-2]:
                i = j + 1
                j = i + 1
                ans += 1
            else:
                j = j + 1
        return ans


if __name__ == '__main__':
    print(f'{Solution.maxSubstrings("abcdeafdef") = }')
    print(f'{Solution.maxSubstrings("bcdaaaab") = }')
