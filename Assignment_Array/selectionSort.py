# Method Implementation using SELECTION SORT

def selectionSort(arr):
    n = len(arr)
    for i in range(n):

        # find minimum from given array
        min = i
        for j in range(i+1, n):
            if arr[min] > arr[j]:
                min = j
        
        #swapped happend after every pass
        arr[i], arr[min] = arr[min] , arr[i]
    return arr


# Driver code
arr = [5, 20, 50, 30, 90, 70, 15]
result = selectionSort(arr)
print("Sorted array is : ",result)