class Solution(object):
    def longestPalindrome(self, s):
        longest_str = ""
        
        for i in range(len(s)):
            sub = self.expand1(s, i)
            if len(sub) > len(longest_str):
                longest_str = sub
        for i in range(len(s) - 1):
            sub = self.expand2(s, i)
            if len(sub) > len(longest_str):
                longest_str = sub
        return  longest_str       
            
            
            
    def expand1(self, s,i):
        sub = s[i]
        l = i - 1
        r = i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            sub = s[l] + sub + s[r]
            l -= 1
            r += 1
        return sub
        
    def expand2(self, s,i):
        sub = s[i] + s[i + 1]
        l = i - 1
        r = i + 2
        while l >= 0 and r < len(s) and s[l] == s[r]:
            sub = s[l] + sub + s[r]
            l -= 1
            r += 1
        return sub
        """
        :type s: str
        :rtype: str
        """
        