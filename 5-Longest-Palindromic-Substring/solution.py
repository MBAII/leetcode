class Solution(object):
    def longestPalindrome(self, s):
        
        """
        :type s: str
        :rtype: str
        """
        start = 0
        end = 0
        for i in range(len(s)):
            len1 = self.expand(s,i,i)
            len2 = self.expand(s,i,i+1)
            len_max = max(len1,len2)
            if len_max > end - start:
                start = i - (len_max - 1) / 2
                end = i + len_max / 2
        return s[start:end+1]
        
        
    
    def expand(self,s,l,r):
        while l >= 0 and r < len(s) and s[l]==s[r]:
            l -= 1
            r += 1
        return r - l - 1