class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sub = ""
        length = 0
        longest = 0
        longest_str = ""
        for c in s:
            if c in sub:
                index = sub.find(c)
                if length > longest:
                    longest = length
                    longest_str = sub
                sub = sub[index+1:] + c
                length = length - index
            else:
                sub += c
                length +=1
        if length > longest:
            return length
        return longest
                