digits = [1,2,3]

class Solution:
    def plusOne(self,digits):
        num = 0
        for digit in digits:
            num = num * 10 + digit

        num += 1
        result = [int(digit) for digit in str(num)]
        return result
    
S1 = Solution()
result = S1.plusOne(digits)
print(result)