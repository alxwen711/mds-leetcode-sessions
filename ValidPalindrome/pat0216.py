import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        s = re.sub(r'[^A-Za-z0-9]','',s)
        left =0
        right = len(s) - 1
        return s == s[::-1]
