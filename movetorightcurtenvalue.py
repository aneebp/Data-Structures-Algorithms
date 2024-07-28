arr = [6,4,3,6,3,6,3,6]
print(arr)
i = 0
j = len(arr)-1
 
while i < j:
    while i<j and arr[i] != 6:
         i=i+1
    while i<j and arr[j] ==6:
        j=j-1
    if i<j:
        arr[i],arr[j] = arr[j],arr[i]
print(arr)