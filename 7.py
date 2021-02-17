"""Question:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]"""

D=[int(i) for i in input("enter the dimensions of the array in a ',' seperated sequence:").split(',')]
row,col=D
print("row=%d and col=%d"%(row,col))
# a=[[0]*col]*row
a=[[0 for j in range(col)]for i in range(row)]
print("initialized array:")
print(a)
for i in range(row):
    # print("\n")
    for j in range(col):
        # print(i,j)
        a[i][j]=i*j
print("final array:")
print(a)
