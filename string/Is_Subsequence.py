class Solution:
    def isSubsequence(self,s,t):
        index = 0
        for char in t:
             #if the s string character is same as the t string character
             if index < len(s) and s[index] == char:
                 index += 1
        return len(s) == index



s = "abc" 
t = "ahbgdc"
S1 = Solution()
result = S1.isSubsequence(s,t)
print(result)