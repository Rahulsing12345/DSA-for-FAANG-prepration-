# Method Implementation using INSERTION SORT
def insertionSort(arr):
    n = len(arr)

    
    for i in range(1, n):
        temp = arr[i]

        j = i-1
        while j>=0 and temp < arr[j]:
            arr[j+1] = arr[j]
            j = j-1
        arr [j+1] = temp
    


# Driver Code
arr = [50, 40, 14, 16, 5, 10]
insertionSort(arr)
print("Sorted array : ",arr)