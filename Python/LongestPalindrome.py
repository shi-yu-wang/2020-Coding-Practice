class Solution:
    """
    @param s: input string
    @return: a string as the longest palindromic substring
    """
    def longestPalindrome(self, s):
        # write your code here
        if not s:
           return ""
        
        n=len(s)
        isPralindrom = [[False] * n for _ in range(n)]
        
        for i in range(n):
            isPralindrom[i][i] = True
        for i in range(1, n):
            isPralindrom[i][i - 1] = True
            
        longest, start, end = 1, 0, 0
        for length in range(1, n):
            for i in range(n - length):
                j = i + length
                isPralindrom[i][j] = s[i] == s[j] and isPralindrom[i + 1][j - 1]
                if isPralindrom[i][j] and length + 1 > longest:
                    longest = length + 1 
                    start, end = i, j
        
        return s[start:end + 1]
