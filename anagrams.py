
class Solution:
    def isAnagram(self, s, t):
        # return Counter(s) == Counter(t)
        # return sorted(s) == sorted(t)
        if len(s) != len(t):
            return False
        
        ctS = {}
        ctT = {}

        for i in range(len(s)):
            ctS[s[i]] = 1 + ctS.get(s[i], 0)
            ctT[t[i]] = 1 + ctT.get(t[i], 0)

        return ctS == ctT
    