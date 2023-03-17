a=1
x=0
k=a
for i in range(31):
    if a&(1<<i):
        k=k-2**i
    else:
        x=x^(1<<i)
    if k==0:
        print(x^2**(i+1))

