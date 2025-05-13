MOD = 1000000007


class Solution:
    @staticmethod
    def lengthAfterTransformations(s: str, t: int) -> int:
        cnt = [0] * 26
        temp = [0] * 26
        for c in s:
            cnt[ord(c) - 97] += 1
        m, n = t % 26, t // 26  # 得到轮数和需要单独处理的轮次，26次变换为一轮

        while n:
            for i in range(26):  # 更新每轮字母的新个数
                temp[i] = cnt[i] + cnt[i - 1]
            temp[2] += cnt[-1]
            for j in range(26):  # 更新下一轮的计数
                cnt[j] = temp[j] % MOD

        return (sum(cnt) + sum(cnt[-m:])) % MOD


if __name__ == '__main__':
    print(Solution().lengthAfterTransformations("abcyy", 2))
    print(Solution().lengthAfterTransformations("azbk", 1))
    print(Solution().lengthAfterTransformations("jqktcurgdvlibczdsvnsg", 7517))
