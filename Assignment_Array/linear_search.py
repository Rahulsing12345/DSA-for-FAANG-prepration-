#Function definition...
#Time Complexity = O(n)
#Space Complexity = O(1) 

def linearSearch(arr,x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


#Driver code
arr = [20, 45, 27, 47, 55, 67, 75, 88, 90]
x = 55

#Function calling
result = linearSearch(arr,x)
print("Searching element is at the index", result)

    