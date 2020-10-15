class Solution:
    def longestPalindromeSubseq(self, s):
        if not s:
            return 0
        
        n = len(s)
        
        lengthCount = [[1] * n for _ in range(n)]
        for i in range(n):
            lengthCount[i][i] = 1
        
        for i in range (n - 1):
            if s[i] == s[i + 1]:
                lengthCount[i][i + 1] = 2           

        for length in range(2, n):
            for i in range(n - length):
                j = i + length
                if s[i] == s[j]:
                    lengthCount[i][j] = lengthCount[i + 1][j - 1] + 2 
                else:
                    lengthCount[i][j] = max(lengthCount[i + 1][j - 1], lengthCount[i + 1][j],  lengthCount[i][j - 1])
                    
        return lengthCount[0][n - 1]
