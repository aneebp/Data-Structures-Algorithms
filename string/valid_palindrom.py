import re
class Solution:
    def isPalindrome(self, s):
        # Step 1: Convert to lowercase and remove non-alphanumeric characters from the original string
        processed_string = re.sub(r'[^a-zA-Z0-9]', "", s).lower()
        
        # Step 2: Reverse the processed string
        reverse_value = processed_string[::-1]
        
        # Step 3: Compare the processed string with its reverse
        if processed_string == reverse_value:
            return True
        else:
            return False
    
    

s = "A man, a plan, a canal: Panama"
S1 = Solution()
result = S1.isPalindrome(s)
print(result)