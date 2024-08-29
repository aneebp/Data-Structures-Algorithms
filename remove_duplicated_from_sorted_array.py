class Solution:

    def remove_duplicated(self,arr):
        if not arr:
            return 0
        
        pointer = 1

        for i in range(1, len(arr)):
            if arr[i] != arr[i-1]:
                arr[pointer] = arr[i]
                pointer += 1

        return pointer
 

arr = [1,1,2]
S1= Solution()
length = S1.remove_duplicated(arr=arr)
print(arr[:length])