arr = [1,3,4,5,6,7,7] #7
position =  1 
value = 2

new_arr = [0] * (len(arr) +1 ) #8

for i in range(position):
    new_arr[i] = arr[i]

new_arr[position] = value

for i in range(position,len(arr)):
    new_arr[i +1] = arr[i]
    
print(new_arr)