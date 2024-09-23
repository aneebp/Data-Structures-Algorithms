class Solution:
    def merge(self, num1,m,num2,n):
        # Start from the end of both arrays
        i= m-1
        j=n-1
        k= m+n-1
         # Merge in reverse order
        while i>=0 and j>=0:
            if num1[i] > num2[j]:
                num1[k] = num1[i]
                i -= 1
            else:
                num1[k] = num2[j]
                j -= 1
            k -= 1
       #  If any elements left in nums2, place them in nums1
        while j>=0:
            num1[k] = num2[j]
            j -= 1
            k -= 1


  



num1 = [1,2,3,0,0,0]
num2 = [2,5,6]
m=3
n=3
S1 = Solution()
S1.merge(num1,m,num2,n)
print(num1)