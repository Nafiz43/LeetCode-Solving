class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()

        for i in range(len(s)):

            if(s[i]=='(' or s[i]=='{' or s[i]=='['):
                stack.append(s[i])
            if(len(stack)==0):
                return False
            elif(s[i]==')' and stack.pop()!='('):
                return False
            elif(s[i]=='}' and stack.pop()!='{'):
                return False
            elif(s[i]==']' and stack.pop()!='['):
                return False
        if(len(stack)==0):
          return True
        else:
          return False


s = Solution()
s.isValid("[[]")