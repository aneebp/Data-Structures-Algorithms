class Solution:
    def lengthOfLastWord(self,s):
        Separated_value = s.split()
        return len(Separated_value[-1])


s='hallo world'
S1 = Solution()
result = S1.lengthOfLastWord(s)
print(result)