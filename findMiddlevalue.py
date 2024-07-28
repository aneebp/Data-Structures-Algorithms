card= [1,2,3,4,5,6,7,8,9]
low = 0
#number to find
query = 2
high = len(card) -1
def find_middle_value(arr):
    mid= len(arr) // 2
    return mid
mid =find_middle_value(card
)

if(mid == query):
    print("Mached")
elif(mid > query):
    print("go to left")
    
elif(mid<query):
    print("go to right")