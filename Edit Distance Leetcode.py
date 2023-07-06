class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1, len2 = len(word1), len(word2)
        dp = [[-1] * (len2+1) for _ in range(len1+1)]
        for i in range(len1+1):
            for j in range(len2+1):
                if i == 0:
                    dp[i][j] = j  
                elif j == 0:
                    dp[i][j] = i 
        for i in range(1, len1+1):
            for j in range(1, len2+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        return dp[len1][len2]
