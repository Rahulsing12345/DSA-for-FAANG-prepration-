## Method Definition
def findPowerOfElement(a,n):
    if n == 1:
        return a
    elif n == 0:
        return 1
    else:
        mid = n//2
        b = findPowerOfElement(a,mid)
        result = b*b

        #for even power
        if n % 2 == 0:
            return result
        return result * a



## Driver code
a = 2
n = 17
result = findPowerOfElement(a,n)
print("The Power of an element is : ",result)