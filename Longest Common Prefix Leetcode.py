class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        x = ""
        for i in zip(*strs):
            if len(set(i)) == 1: 
                x += i[0]
            else: 
                return x
        return x
