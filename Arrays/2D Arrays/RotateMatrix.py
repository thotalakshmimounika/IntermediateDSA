#You are given a n x n 2D matrix A representing an image.Rotate the image by 90 degrees (clockwise).

a=[[1,2,3],[4,5,6],[7,8,9]]

n=len(a)
for i in range(len(a)):
    for j in range(i+1,len(a[0])):
        temp=a[i][j]
        a[i][j]=a[j][i]
        a[j][i]=temp
for i in range(len(a)):
    x=0
    y=n-1
    while x<=y:
        temp=a[i][x]
        a[i][x]=a[i][y]
        a[i][y]=temp
        x+=1
        y-=1
print(a)

