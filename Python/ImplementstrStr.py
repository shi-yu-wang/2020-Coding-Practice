class Solution:
    BASE = 1000000
    
    def strStr(self, haystack: str, needle: str):
        if not needle:
            return 0
        if not haystack:
            return -1
        
        m = len(needle)
        n = len(haystack)
        
        # 31^m
        power = 1
        for i in range(m):
            power = power * 31
            
        # target hash code
        targetCode = 0
        for i in range(m):
            targetCode = (targetCode * 31 + ord(needle[i])) % self.BASE
        
        hashCode = 0
        for i in range(n):
            hashCode = (hashCode * 31 + ord(haystack[i])) % self.BASE
            if i < m - 1:
                continue
            
            if i >= m:
                hashCode = hashCode - ord(haystack[i - m]) * power % self.BASE
                if hashCode < 0:
                    hashCode = hashCode + self.BASE
                    
            if hashCode == targetCode:
                if haystack[i - m + 1:i + 1] == needle:
                    return i - m + 1
            
        return -1
