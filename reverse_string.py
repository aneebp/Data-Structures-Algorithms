class Solution(object):
    def reverseString(self, s):
        left = 0
        right = len(s) -1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s



    
s = ["h","e","l","l","o"]
S1 = Solution()
result = S1.reverseString(s)
print(result)

        