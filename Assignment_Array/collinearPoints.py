def collinearPoints(x1,y1,x2,y2,x3,y3):
    if ((y2-y1)*(x3-x2) == (x2-x1)*(y3-y2)):
        print("Yes")
    else:
        print("No")

## Driver code
x1, x2, x3, y1, y2, y3 = 7,9,6,6,8,6
collinearPoints(x1,y1,x2,y2,x3,y3)
