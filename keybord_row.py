class Solution(object):
    def findWords(self, words):
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        result = []
        for word in words:
            cov_lowercase = set(word.lower()) #convert to lowercase and set character
            if cov_lowercase.issubset(row1) or cov_lowercase.issubset(row2) or cov_lowercase.issubset(row3): #looking to each row to find word
                result.append(word)
        return result
            


words =["Hello","Alaska","Dad","Peace"]
S1 = Solution()
result = S1.findWords(words)
print(result)