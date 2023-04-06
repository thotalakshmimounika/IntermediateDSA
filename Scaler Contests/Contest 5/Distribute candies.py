a=13
n=a
while True:
    n+=1
    for x in range(2,n):
        if n%x==0:
            break
    else:
        print(n)