MOD = 1_000_000_007


class Solution:
    @staticmethod
    def lengthAfterTransformations(s: str, t: int) -> int:
        cnt = [0] * 26
        temp = [0] * 26
        for c in s:
            cnt[ord(c) - 97] += 1
        m, n = t % 26, t // 26  # 得到轮数和需要单独处理的轮次，26次变换为一轮

        for _ in range(n):
            for i in range(26):  # 更新每轮字母的新个数
                temp[i] = cnt[i] + cnt[i - 1]
            temp[1] += cnt[-1]
            cnt = [x % MOD for x in temp]

        # 返回值需要特判情况，如果t是26的倍数sum(cnt[-m:])即为sum(cnt)，不应该再加上
        return (sum(cnt) + sum(cnt[-m:])) % MOD if m > 0 else sum(cnt) % MOD


if __name__ == '__main__':
    print(Solution().lengthAfterTransformations("abcyy", 2))
    print(Solution().lengthAfterTransformations("azbk", 1))
    print(Solution().lengthAfterTransformations("oatgwnertmbehheheejbnxgbxz", 7566))
