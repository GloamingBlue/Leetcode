from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = ans = 0
        sdict = defaultdict(int)
        for right, c in enumerate(s):
            sdict[c] += 1
            if sdict[c] > 1:
                while sdict[c] > 1:
                    sdict[s[left]] -= 1
                    left += 1
            else:
                ans = max(ans, right - left + 1) 
        return ans
    

if __name__ == '__main__':
    print(f'{Solution().lengthOfLongestSubstring("abcabcbb") = }')
    print(f'{Solution().lengthOfLongestSubstring("bbbbb") = }')
    print(f'{Solution().lengthOfLongestSubstring("pwwkew") = }')
