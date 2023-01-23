#Given an array A and an integer B, find the number of occurrences of B in A.
a=[1,2,3,4,5,3]
b=3
c=0
for i in a:
    if i==b:
        c+=1
print(c)