class Solution:
    @staticmethod
    def smallestEquivalentString(s1: str, s2: str, baseStr: str) -> str:
        dic = []  # 存储字母间对应关系的划分，划分是集合
        flag = [-1] * 26  # 记录字母是否出现过，未出现记为-1；出现过记为所处集合的下标
        for i, s in enumerate(s1):
            x, y = flag[ord(s) - 97], flag[ord(s2[i]) - 97]
            if x == y == -1:  # 二者都未出现过
                dic.append({s, s2[i]})
                flag[ord(s) - 97] = flag[ord(s2[i]) - 97] = len(dic) - 1  # 更新下标
            elif x != -1 and y == -1:  # 出现了一个
                dic[x].add(s2[i])
                flag[ord(s2[i]) - 97] = x  # 更新下标
            elif y != -1 and x == -1:  # 出现了一个
                dic[y].add(s)
                flag[ord(s) - 97] = y  # 更新下标
            elif x == y:  # 已经添加过关系
                continue
            else:  # 二者都出现过，但是不在一个划分，此时需要对划分进行合并
                dic[x] |= dic[y]
                for j in dic[y]:
                    flag[ord(j) - 97] = x  # 更新下标，这样没有字母会指向原来的集合了，也不用对其进行清理

        k = list(set(flag))  # 获得所有划分的下标，注意刨除-1
        for f in k:  # 对划分进行排序
            if f != -1:
                dic[f] = sorted(dic[f])
        ans = ''
        for b in baseStr:
            if flag[ord(b) - 97] == -1:
                ans += b
            else:
                ans += dic[flag[ord(b) - 97]][0]
        return ans


if __name__ == '__main__':
    print(f'{Solution().smallestEquivalentString("parker", "morris", "parser") = }')
    print(f'{Solution().smallestEquivalentString("hello", "world", "hold") = }')
    print(f'{Solution().smallestEquivalentString("leetcode", "programs", "sourcecode") = }')
