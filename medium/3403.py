class Solution:
    @staticmethod
    def answerString(word: str, numFriends: int) -> str:
        if numFriends == 1:  # 如果只有一个朋友，只有一种分法
            return word
        n = len(word)
        maxLen = n - numFriends + 1  # 最大串的长度
        l, maxStr = 0, ''
        while l < n:
            if l + maxLen <= len(word):
                maxStr = max(maxStr, word[l:l + maxLen])
            else:
                maxStr = max(maxStr, word[l:])
            l += 1
        return maxStr


if __name__ == '__main__':
    print(f'{Solution().answerString("dbca", 2) = }')
    print(f'{Solution().answerString("gggg", 4) = }')
    print(f'{Solution().answerString("gh", 1) = }')
