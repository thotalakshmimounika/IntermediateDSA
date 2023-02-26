#Construct a binary number a 1's followed by b 0's. Return the decimal value of that number
a=5
b=4
c=a+b
ans=0
l=0
for i in range(c-1,b-1,-1):
    ans=ans|(1<<i)
print(ans)