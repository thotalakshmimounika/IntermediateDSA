#You are given a 2D integer matrix A, make all the elements in a row or column zero if the A[i][j] = 0. Specifically, make entire ith row and jth column zero.
a= [[1,2,3,4],[5,6,7,0],[9,2,0,4]]
rind=[]
cind=[]
for i in range(len(a)):
    for j in range(len(a[0])):
        if a[i][j]==0:
            rind.append(i)
            cind.append(j)
            print(cind,rind)
print(cind,rind)
for i in rind:
    for j in range(len(a[0])):
        a[i][j]=0
print(a)
for i in cind:
    for j in range(len(a)):
        a[j][i]=0
print(a)