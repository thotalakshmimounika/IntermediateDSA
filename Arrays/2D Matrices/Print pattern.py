x=0
n=7
while(x<=n-x):
    for j in range(n):
        if x==0:
            print("0 ",end='')
        else:
            if j<x or j>n-1-x:
                print("0 ",end='')
            else:
                print("1 ",end='')
    print("")
    x+=1
while (x<n):
    for j in range(n):
        if x==n-1:
            print("0 ",end='')
        else:
            if j<n-1-x or j>x:
                print("0 ",end='')
            else:
                print("1 ",end='')
    print("")
    x+=1 


        
