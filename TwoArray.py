num = [2,7,11,15]
target = 9

found = ""
class Solution:
    def twoSum(self,num,target):
        for i in range(len(num) -1):
            for j in range(i+1,len(num)):
                if num[i] + num[j] == target:
                    return [i,j]


  

Sl = Solution()
resulf = Sl.twoSum(num,target)
print(resulf)

    

