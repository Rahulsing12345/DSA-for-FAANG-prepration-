## iterative approach

# Function definition...
def binarySearch(arr, x,  left, right):

    while left<= right:                                               # check array is not empty
        
        mid = left + (right-left)//2                                  # or    mid = (left + right)//2  
        if arr[mid] == x:
            return mid
        
        elif arr[mid] < x:
            left = (mid+1)
            
        
        else:
            right = (mid-1)
            

    # Searching element is not present in given Array
    return -1

#driver code
arr =  [20, 30, 40, 50, 60, 70, 80, 90]
x = 20
left = 0
right = len(arr)-1

#Function calling....
result = binarySearch(arr,x,  left, right)
print("Searching element is at the index", result)