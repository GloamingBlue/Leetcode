import typing


class Solution:
    @staticmethod
    def idealArrays(n: int, maxValue: int) -> int:
        # 预处理阶乘和逆元
        def prepare_factorials(N, MOD):
            fac = [1] * (N + 1)
            inv = [1] * (N + 1)
            for i in range(1, N + 1):
                fac[i] = fac[i - 1] * i % MOD
            inv[N] = pow(fac[N], MOD - 2, MOD)
            for i in range(N - 1, -1, -1):
                inv[i] = inv[i + 1] * (i + 1) % MOD
            return fac, inv

        def comb(n, k, fac, inv):
            if n < k or k < 0:
                return 0
            return fac[n] * inv[k] % MOD * inv[n - k] % MOD

        MOD = 10 ** 9 + 7
        fac, inv = prepare_factorials(n + 10000, MOD)  # 预处理足够大的阶乘
        # 预处理每个数的质因数分解
        spf = [0] * (maxValue + 1)
        for i in range(2, maxValue + 1):
            if spf[i] == 0:
                for j in range(i, maxValue + 1, i):
                    if spf[j] == 0:
                        spf[j] = i
        ans = 0
        for x in range(1, maxValue + 1):
            y = x
            factors = {}
            while y > 1:
                p = spf[y]
                cnt = 0
                while y % p == 0:
                    y //= p
                    cnt += 1
                factors[p] = cnt
            res = 1
            for cnt in factors.values():
                res = res * comb(n - 1 + cnt, cnt, fac, inv) % MOD
            ans = (ans + res) % MOD
        return ans
    

if __name__ == '__main__':
    print(Solution.idealArrays(5, 3))
