class Solution:
    @staticmethod
    def resultingString(s: str) -> str:
        if len(s) <= 1:
            return s
        # 97 - 122
        i = 1
        while i < len(s):
            if abs(ord(s[i]) - ord(s[i-1])) == 1 or abs(ord(s[i]) - ord(s[i-1])) == 25:
                s = s[:i-1] + s[i+1:]
                if i > 1:
                    i -= 1
            else:
                i += 1
        return s


if __name__ == '__main__':
    print(f'{Solution.resultingString("fghji") = }')
    print(f'{Solution.resultingString("adcb") = }')
    print(f'{Solution.resultingString("zadb") = }')
    print(f'{Solution.resultingString("abc") = }')
