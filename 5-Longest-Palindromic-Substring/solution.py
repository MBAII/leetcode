class Solution(object):
    def longestPalindrome(self, s):
        longest_str = ""
        
        for i in range(len(s)):
            sub1 = self.expand1(s, i)
            sub2 = self.expand2(s, i)
            if len(sub1) > len(longest_str):
                longest_str = sub1
            if len(sub2) > len(longest_str):
                longest_str = sub2
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
        l = i - 1
        r = i + 2
        if l >= 0 or r < len(s):
            return ""
        sub = s[i] + s[i + 1]
        while l >= 0 and r < len(s) and s[l] == s[r]:
            sub = s[l] + sub + s[r]
            l -= 1
            r += 1
        return sub
        """
        :type s: str
        :rtype: str
        """
        