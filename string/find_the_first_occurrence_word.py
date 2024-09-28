class Solution:
    def strStr(self,haystack,needle):
        # find method to find the first occurrence of needle
        find_value = haystack.find(needle)
        # If the needle is not found, the find() method returns -1.
        return find_value
        
        

haystack = "sadbutsad"
needle = "sad"
S1 = Solution()
result = S1.strStr(haystack,needle)
print(result)