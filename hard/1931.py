import numpy as np


MOD = 1_000_000_007


class Solution:
    @staticmethod
    def colorTheGrid(m: int, n: int) -> int:
        pow3 = [3 ** i for i in range(m)]  # 预处理得到3的幂
        valid = []  # 初始化所有合理的三进制数
        for i in range(3 ** m):  # 遍历所有可能的m位三进制数
            for j in range(1, m):  # 对每一位进行检测，for-else结构
                if i // pow3[j] % 3 == i // pow3[j - 1] % 3:
                    break
            else:  # 只有for未被break打断，才会执行else
                valid.append(i)

        v = len(valid)  # 合理三进制数个数
        f0 = np.ones((v, 1), dtype=object)  # 初始化递归边界列向量，设置数据类型为对象类型，防止计算过程中数据溢出，但是会降低计算速度
        mapNxt = np.zeros((v, v), dtype=object)  # 初始化映射矩阵，设置数据类型为对象类型，防止计算过程中数据溢出，但是会降低计算速度
        for i, a in enumerate(valid):  # 更新映射矩阵
            for j, b in enumerate(valid):
                for k in range(m):
                    if a // pow3[k] % 3 == b // pow3[k] % 3:
                        break
                else:
                    mapNxt[i, j] = 1

        return np.sum(Solution.pow(mapNxt, n - 1, f0)) % MOD

    @staticmethod
    def pow(m: np.ndarray, n: int, f0: np.ndarray) -> np.ndarray:
        """实现矩阵快速幂和取模"""
        while n:
            if n & 1:
                f0 = m @ f0 % MOD
            m = m @ m % MOD
            n >>= 1
        return f0


if __name__ == '__main__':
    print(Solution.colorTheGrid(1, 1))
    print(Solution.colorTheGrid(1, 2))
    print(Solution.colorTheGrid(5, 5))
