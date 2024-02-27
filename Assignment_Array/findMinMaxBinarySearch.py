## Method Definition
def findMaxandMin(arr, i, j):
    # single element condition
    if i == j:
        max_val = arr[i]
        min_val = arr[i]

    # Two element condition
    elif i == j-1:
        if arr[i] < arr[j]:
            max_val = arr[j]
            min_val = arr[i]

        else:
            max_val = arr[i]
            min_val = arr[j]

    else:
        ## Divide and conquer approach
        ## 1. Divide
        mid = i +(j-i)//2

        ## 2. Recursion ->  Conquer
        max_1, min_1 = findMaxandMin(arr, i, mid)
        max_2, min_2 = findMaxandMin(arr, mid+1, j)
        
        ## 3. Combine
        if max_1 < max_2:
            max_val = max_2
        else:
            max_val = max_1
        
        if min_1 < min_2:
            min_val = min_1
        else:
            min_val = min_2
    return max_val, min_val

## Driver code
arr = [20, 39, 45, 65, 21, 44, 89, 92]
i = 0                                                                ##   i is Starting index
j = (len(arr) - 1)                                                   ##   j is ending index
## function calling
max_val, min_val = findMaxandMin(arr, i, j)
print("Max and Min value is", max_val, min_val)