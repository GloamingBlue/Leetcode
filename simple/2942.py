from typing import List


class Solution:
    @staticmethod
    def findWordsContaining(words: List[str], x: str) -> List[int]:
        return [i for i, s in enumerate(words) if x in s]


if __name__ == '__main__':
    print(f'{Solution.findWordsContaining(words=["leet", "code"], x="e") = }')
    print(f'{Solution.findWordsContaining(words=["abc", "bcd", "aaaa", "cbc"], x="a") = }')
