#Given an integer array A containing N distinct integers, you have to find all the leaders in array A.An element is a leader if it is strictly greater than all the elements to its right side.
#Note The rightmost element is always a leader.

a= [16, 17, 4, 3, 5, 2]
n=len(a)
maxele=a[n-1]
print(n,maxele)
ans=[a[n-1]]
for i in range(n-1,-1,-1):
    if a[i]>maxele:
        maxele=a[i]
        ans.append(maxele)
print(ans)

