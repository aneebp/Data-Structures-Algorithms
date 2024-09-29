class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        # Start by assuming the first string is the common prefix
        prefix = strs[0]

        for s in strs[1:]:
           # We compare it with "flow". The common prefix between "flower" 
            while s[:len(prefix)] != prefix:
                #Since "flower" is not a common prefix, we reduce "flower" by removing its last character, so it becomes "flowe".
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
        
        


strs = ["flower","flow","flight"]
S1 = Solution()
result =S1.longestCommonPrefix(strs)
print(result)