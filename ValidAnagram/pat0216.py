class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_S = {}
        hash_T = {}
        
        if len(s) != len(t):
            return False
        else:
            for i in range(0, len(s)):
                hash_S[s[i]] = 0
                hash_T[t[i]] = 0
            for i in range(0, len(s)):

                if hash_S[s[i]] >=1:
                    hash_S[s[i]] +=1 
                else:
                    hash_S[s[i]] = 1

                if hash_T[t[i]] >=1:
                    hash_T[t[i]] +=1 
                else:
                    hash_T[t[i]] = 1
           
            if hash_S == hash_T:
                return True
            else:
                return False
