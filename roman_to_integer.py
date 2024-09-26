class Solution:
    def romanToInt(self, s):
       roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
       n = len(s)
       total = 0
       
       for i in range(n):
           if i<n-1 and roman_map[s[i]] < roman_map[s[i +1]]:
               total -= roman_map[s[i]]
           else:
               total += roman_map[s[i]]
       return total               
               




s = "XII"
S1= Solution()
result = S1.romanToInt(s)
print(result)